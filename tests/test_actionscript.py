import io
import json
import os
import shutil
import struct
import tempfile
import threading
import time
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from wot_extractor.actionscript import ASOptions, find_ffdec, run_actionscript
from wot_extractor.actionscript import engine as as_engine
from wot_extractor.actionscript import ffdec as ffdec_mod
from wot_extractor.actionscript.ffdec import ExportRun, FFDec
from wot_extractor.config import load_config
from wot_extractor.detect.install import inspect_install
from wot_extractor.extract import ExtractOptions, ManifestError, run_extract
from wot_extractor.extract.writer import long_path
from wot_extractor.formats.abc import AbcError, class_declaration, parse_abc
from wot_extractor.formats.swf import SwfError, decompress, parse_swf, swf_from_container

from .helpers import make_install
from .swfgen import make_abc, make_swf, sample_swf, tag

_FF = None


def real_ffdec():
    global _FF
    if _FF is None:
        _FF = find_ffdec()
    return _FF[0]


def swc(swf: bytes) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("catalog.xml", "<swc/>")
        zf.writestr("library.swf", swf)
    return buf.getvalue()


class SwfParserTests(unittest.TestCase):
    def test_compressions_and_catalog(self):
        for comp, sig in (("zlib", "CWS"), ("lzma", "ZWS"), ("none", "FWS")):
            with self.subTest(comp=comp):
                info, _ = parse_swf(sample_swf(comp))
                self.assertEqual(info.signature, sig)
                self.assertEqual(info.code_kind, "as3")
                self.assertTrue(info.as3)
                self.assertEqual(info.background, "#102030")
                self.assertEqual([c["name"] for c in info.classes], ["net.test.Foo"])
                self.assertEqual(info.classes[0]["extends"], "flash.display.Sprite")
                self.assertEqual(info.imports, [{"url": "lib.swf", "symbols": [{"id": 5, "name": "Btn"}]}])
                self.assertEqual(info.exports, [{"id": 2, "name": "Panel"}])
                self.assertEqual(info.symbol_classes, [{"id": 0, "class": "net.test.Foo"}])
                self.assertEqual(info.fonts[0]["name"], "Arial")
                self.assertEqual(info.frame_labels, ["start"])
                self.assertEqual(info.frame_rate, 30.0)
                self.assertFalse(info.errors or info.warnings)
                d = info.to_dict()
                self.assertEqual(d["counts"]["classes"], 1)
                json.dumps(d)

    def test_limits_and_bad_input(self):
        with self.assertRaises(SwfError):
            decompress(b"XYZ\x0a" + struct.pack("<I", 100) + b"\0" * 10)
        with self.assertRaises(SwfError):
            decompress(b"CWS\x0a" + struct.pack("<I", 2**31))  # tamanho declarado acima do limite
        with self.assertRaises(SwfError):
            decompress(b"CWS\x0a" + struct.pack("<I", 100) + b"nao e zlib")

    def test_truncated_tag_is_warning(self):
        data = sample_swf("none")
        info, _ = parse_swf(data[:-30])
        self.assertTrue(info.warnings)

    def test_corrupt_abc_is_component_error(self):
        bad = tag(82, struct.pack("<I", 1) + b"x\x00" + make_abc()[:40])
        info, _ = parse_swf(make_swf([tag(69, bytes([8, 0, 0, 0])), bad, tag(1, b"")]))
        self.assertEqual(info.code_kind, "as3")
        self.assertTrue(info.errors)
        self.assertIn("error", info.abc[0])

    def test_no_code(self):
        info, _ = parse_swf(sample_swf(with_abc=False))
        self.assertEqual(info.code_kind, "none")

    def test_swc(self):
        inner, name = swf_from_container(swc(sample_swf()), "lib.swc")
        self.assertEqual(name, "library.swf")
        self.assertEqual(parse_swf(inner)[0].code_kind, "as3")
        with self.assertRaises(SwfError):
            swf_from_container(b"nao zip", "x.swc")


class AbcTests(unittest.TestCase):
    def test_declarations(self):
        abc = parse_abc(make_abc(extra_method_names=True))
        name, text = class_declaration(abc, 0, "sources/res/x.swf")
        self.assertEqual(name, "net.test.Foo")
        self.assertIn("package net.test {", text)
        self.assertIn("import flash.display.Sprite;", text)
        self.assertIn("public class Foo extends Sprite", text)
        self.assertIn('public function run(a:int, b:String = "x"):void', text)
        self.assertIn("public static const LIMIT:int;", text)
        self.assertIn("DECLARACOES", text)

    def test_rejects_bad_abc(self):
        data = make_abc()
        with self.assertRaises(AbcError):
            parse_abc(data[:2] + struct.pack("<H", 47) + data[4:])  # versao
        for cut in (10, len(data) // 2, len(data) - 1):
            with self.subTest(cut=cut), self.assertRaises(AbcError):
                parse_abc(data[:cut])
        with self.assertRaises(AbcError):
            parse_abc(data + b"\x00")  # bytes a mais


class _Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(self.tmp), ignore_errors=True))
        self.pkgs = {"gui-part1.pkg": {
            "gui/flash/app.swf": sample_swf(),
            "gui/flash/anim.swf": sample_swf(with_abc=False),
            "gui/flash/broken.swf": b"CWS\x0a" + struct.pack("<I", 500) + b"lixo",
            "gui/flash/swc/lib.swc": swc(sample_swf("none")),
        }}
        self.cfg = load_config(project_root=self.tmp)
        self.cfg.output_root = self.tmp / "out"
        self.out = self.cfg.realm_output_dir("EU")

    def _extract(self, pkgs=None, prune=False):
        root = make_install(self.tmp / "game", pkgs=pkgs or self.pkgs)
        return run_extract(self.cfg, inspect_install(root, ["cli"], deep=False),
                           ExtractOptions(jobs=2, prune=prune))

    def _manifest(self):
        return json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))


class EngineNoFFDecTests(_Base):
    def _run(self, **kw):
        kw.setdefault("jobs", 2)
        return run_actionscript(self.cfg, "EU", ASOptions(use_ffdec=False, **kw))

    def test_requires_manifest(self):
        with self.assertRaises(ManifestError):
            self._run()

    def test_cycle(self):
        self._extract()
        r = self._run()
        self.assertEqual(r.totals, {"partial": 2, "extracted": 1, "failed": 1})
        e = self._manifest()["entries"]
        a = e["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual((a["status"], a["code"], a["scripts"]["kind"]), ("partial", "as3", "declarations"))
        self.assertIn("so declaracoes", a["error"])
        decl = self.out / "sources_as/scripts/res/gui/flash/app.swf/net/test/Foo.as"
        self.assertIn("public class Foo extends Sprite", decl.read_text(encoding="utf-8"))
        cat = json.loads((self.out / "sources_as/swf/res/gui/flash/app.swf.json").read_text(encoding="utf-8"))
        self.assertEqual((cat["source"], cat["actionscript"]), ("sources/res/gui/flash/app.swf", "as3"))
        self.assertEqual(e["res/gui/flash/anim.swf"]["actionscript"]["status"], "extracted")
        self.assertEqual(e["res/gui/flash/broken.swf"]["actionscript"]["status"], "failed")
        lib = e["res/gui/flash/swc/lib.swc"]["actionscript"]
        self.assertEqual(lib["code"], "as3")
        self.assertTrue((self.out / "sources_as/scripts/res/gui/flash/swc/lib.swc/net/test/Foo.as").is_file())
        index = json.loads((self.out / "sources_as/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(sorted(index["classes"]["net.test.Foo"]),
                         ["res/gui/flash/app.swf", "res/gui/flash/swc/lib.swc"])
        self.assertTrue((self.out / "actionscript_report.json").is_file())
        self.assertFalse((self.out / ".state/as_tmp").exists())

        r2 = self._run()
        self.assertEqual((r2.to_process, sum(r2.unchanged.values())), (0, 4))
        self.assertEqual(self._run(retry=True).to_process, 3)  # partial/failed

        self._extract()  # extract incremental preserva o estado
        self.assertIn("actionscript", self._manifest()["entries"]["res/gui/flash/app.swf"])
        pkgs = {"gui-part1.pkg": dict(self.pkgs["gui-part1.pkg"])}
        del pkgs["gui-part1.pkg"]["gui/flash/app.swf"]
        self._extract(pkgs, prune=True)  # --prune apaga tambem as saidas do SWF removido
        self.assertFalse((self.out / "sources_as/swf/res/gui/flash/app.swf.json").exists())
        self.assertFalse((self.out / "sources_as/scripts/res/gui/flash/app.swf").exists())

    def test_dry_run_and_filters(self):
        self._extract()
        r = self._run(dry_run=True)
        self.assertEqual((r.selected, r.to_process), (4, 4))
        self.assertFalse((self.out / "sources_as/catalog.json").exists())
        self.assertEqual(self._run(globs=("*app.swf",)).selected, 1)


class EngineFakeFFDecTests(_Base):
    """Logica de integracao com o FFDec, com uma exportacao simulada."""

    FF = FFDec(Path("java"), Path("ffdec-cli.jar"), "99.0")

    def _fake_export(self, body: str, missing=False, rc=0, timed_out=False, oom=False):
        def export(ff, swf, out_dir, items, timeout, mt, ct):
            if "script" in items and not timed_out:
                d = out_dir / "scripts" / "net" / "test"
                d.mkdir(parents=True)
                if not missing:
                    (d / "Foo.as").write_text(body, encoding="utf-8")
                else:
                    (d / "Other.as").write_text(body, encoding="utf-8")
            if "symbolClass" in items:
                (out_dir / "symbolClass").mkdir(parents=True, exist_ok=True)
                (out_dir / "symbolClass" / "symbols.csv").write_text("0;net.test.Foo", encoding="utf-8")
            return ExportRun(rc, 0.1, timed_out, "log", oom)
        return export

    def _run(self, export, **kw):
        with mock.patch.object(ffdec_mod, "export", export):
            return run_actionscript(self.cfg, "EU", ASOptions(globs=("*app.swf",), jobs=1, **kw), ff=self.FF)

    def test_success(self):
        self._extract()
        r = self._run(self._fake_export("package net.test { public class Foo {} }"))
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual((a["status"], a["scripts"]["kind"], a["scripts"]["tool"]), ("success", "decompiled", "FFDec 99.0"))
        self.assertEqual(a["assets"]["symbolClass"], 1)
        self.assertTrue((self.out / "sources_as/scripts/res/gui/flash/app.swf/net/test/Foo.as").is_file())
        self.assertTrue((self.out / "sources_as/assets/res/gui/flash/app.swf/symbolClass/symbols.csv").is_file())
        self.assertEqual(r.totals, {"success": 1})

    def test_markers_missing_and_failure(self):
        self._extract()
        body = 'function f() { throw new IllegalOperationError("Not decompiled due to timeout"); }\n§§push(1);\n'
        self._run(self._fake_export(body))
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual(a["status"], "partial")
        self.assertEqual((a["scripts"]["methods_not_decompiled"], a["scripts"]["unstructured_lines"]), (1, 1))
        self._run(self._fake_export("x", missing=True), force=True)
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual((a["status"], a["scripts"]["missing_classes"]), ("partial", 1))
        # a classe em falta fica com as declaracoes do ABC, ao lado do que o FFDec exportou
        self.assertEqual(a["scripts"]["declarations_for_missing"], 1)
        base = self.out / "sources_as/scripts/res/gui/flash/app.swf/net/test"
        self.assertIn("DECLARACOES", (base / "Foo.as").read_text(encoding="utf-8"))
        self.assertEqual((base / "Other.as").read_text(encoding="utf-8"), "x")
        # Java sem memoria: mensagem explicita
        self._run(self._fake_export("x", missing=True, rc=1, oom=True), force=True)
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertIn("sem memoria", a["error"])
        # FFDec excede o tempo: recorre as declaracoes
        self._run(self._fake_export("x", timed_out=True), force=True)
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual((a["status"], a["scripts"]["kind"]), ("partial", "declarations"))
        self.assertIn("tempo limite", a["error"])

    def test_case_colliding_packages(self):
        """net.test.VO e net.test.vo partilham uma pasta no Windows: nao sao classes em falta e as declaracoes
        nunca substituem o codigo do FFDec."""
        abc = make_abc((("net.test", "Foo", "flash.display", "Sprite"), ("net.test.VO", "Bar", "", "Object"),
                        ("net.test.vo", "Baz", "", "Object")))
        swf = make_swf([tag(69, bytes([0x08, 0, 0, 0])), tag(82, struct.pack("<I", 1) + b"f\x00" + abc), tag(1, b"")])
        self._extract({"gui-part1.pkg": {"gui/flash/app.swf": swf}})

        def export(ff, swf, out_dir, items, timeout, mt, ct):
            d = out_dir / "scripts" / "net" / "test"
            (d / "VO").mkdir(parents=True)
            (d / "Foo.as").write_text("ffdec Foo", encoding="utf-8")
            (d / "VO" / "Bar.as").write_text("ffdec Bar", encoding="utf-8")
            (d / "VO" / "Baz.as").write_text("ffdec Baz", encoding="utf-8")  # pacote 'vo' na pasta 'VO'
            return ExportRun(0, 0.1, False, "log")

        self._run(export, assets=False)
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual((a["status"], a["scripts"]["missing_classes"]), ("success", 0), a)
        self.assertEqual(a["scripts"]["case_collisions"], [["net.test.VO", "net.test.vo"]])
        base = self.out / "sources_as/scripts/res/gui/flash/app.swf/net/test"
        self.assertEqual((base / "VO" / "Baz.as").read_text(encoding="utf-8"), "ffdec Baz")
        # declaracoes so para o que nao existe, mesmo com a outra caixa no caminho
        n = as_engine._write_declarations("res/gui/flash/app.swf", swf, self.out,
                                          only={"net/test/vo/Baz.as", "net/test/Foo.as"})
        self.assertEqual(n["files"], 0)
        self.assertEqual((base / "VO" / "Baz.as").read_text(encoding="utf-8"), "ffdec Baz")

    def test_tool_change_reprocesses(self):
        self._extract()
        self._run(self._fake_export("package net.test { public class Foo {} }"))
        r = self._run(self._fake_export("package net.test { public class Foo {} }"))
        self.assertEqual(r.to_process, 0)
        self.FF = FFDec(Path("java"), Path("ffdec-cli.jar"), "100.0")
        r = self._run(self._fake_export("package net.test { public class Foo {} }"))
        self.assertEqual(r.to_process, 1)


class SchedulingTests(_Base):
    def test_heavy_limit_and_order(self):
        self._extract()
        lock = threading.Lock()
        state = {"now": 0, "max": 0, "order": []}

        def export(ff, swf, out_dir, items, timeout, mt, ct):
            with lock:
                state["now"] += 1
                state["max"] = max(state["max"], state["now"])
                state["order"].append(swf.name)
            time.sleep(0.2)
            with lock:
                state["now"] -= 1
            return ExportRun(0, 0.2, False, "log")

        with mock.patch.object(ffdec_mod, "export", export):
            # limiar 1 byte: todos os SWF com ABC contam como pesados
            run_actionscript(self.cfg, "EU", ASOptions(jobs=4, heavy_jobs=1, heavy_abc_bytes=1, assets=False),
                             ff=EngineFakeFFDecTests.FF)
        self.assertEqual(state["max"], 1)
        self.assertEqual(len(state["order"]), 2)  # app.swf e o library.swf do .swc

    def test_move_dir_retries_on_lock(self):
        src = self.tmp / "a"
        (src / "x").mkdir(parents=True)
        (src / "x" / "f.as").write_text("1", encoding="utf-8")
        real = os.replace
        calls = {"n": 0}

        def flaky(a, b):
            calls["n"] += 1
            if calls["n"] < 3:
                raise PermissionError(5, "Acesso negado")
            return real(a, b)

        with mock.patch.object(as_engine.os, "replace", flaky), mock.patch.object(as_engine.time, "sleep"):
            as_engine._move_dir(src, self.tmp / "b" / "c")
        self.assertTrue((self.tmp / "b/c/x/f.as").is_file())
        self.assertFalse(src.exists())
        # bloqueio persistente: copia e apaga
        (src / "y").mkdir(parents=True)
        (src / "y" / "g.as").write_text("2", encoding="utf-8")
        with mock.patch.object(as_engine.os, "replace", side_effect=PermissionError(5, "x")), \
                mock.patch.object(as_engine.time, "sleep"):
            as_engine._move_dir(src, self.tmp / "b" / "c")
        self.assertTrue((self.tmp / "b/c/y/g.as").is_file())
        self.assertFalse(src.exists())


@unittest.skipUnless(real_ffdec() is not None, "FFDec nao instalado")
class RealFFDecTests(_Base):
    def test_real_export(self):
        self._extract()
        r = run_actionscript(self.cfg, "EU", ASOptions(globs=("*app.swf",), jobs=1, timeout=300), ff=real_ffdec())
        a = self._manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
        self.assertEqual(a["scripts"]["kind"], "decompiled", a)
        text = (self.out / "sources_as/scripts/res/gui/flash/app.swf/net/test/Foo.as").read_text(encoding="utf-8")
        self.assertIn("class Foo extends Sprite", text)
        self.assertIn("function run(", text)
        self.assertEqual(r.totals.get("success"), 1, a)


if __name__ == "__main__":
    unittest.main()
