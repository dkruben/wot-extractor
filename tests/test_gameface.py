import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from wot_extractor.config import load_config
from wot_extractor.detect.install import inspect_install
from wot_extractor.extract import ExtractOptions, ManifestError, run_extract
from wot_extractor.extract.writer import long_path
from wot_extractor.formats.jsfmt import (FormatError, format_css, format_js, format_tokens, is_minified,
                                         tokenize_css, tokenize_js)
from wot_extractor.gameface import GFOptions, find_node, run_gameface
from wot_extractor.gameface import analyze as gf_analyze
from wot_extractor.gameface.analyze import js_references, webpack_info
from wot_extractor.gameface.pylinks import snake

from .helpers import make_install


def vals(src):
    return [(t.type, t.value) for t in tokenize_js(src)]


class LexerTests(unittest.TestCase):
    def test_regex_vs_division(self):
        self.assertIn(("re", "/b/g"), vals("x=a.replace(/b/g,'c')"))
        self.assertEqual([v for _, v in vals("a/b/c")], ["a", "/", "b", "/", "c"])
        self.assertIn(("p", "/"), vals("(a+b)/2"))
        self.assertIn(("re", "/^\\s+$/"), vals("for(const[r]of n)/^\\s+$/.test(r)&&f()"))
        self.assertIn(("re", "/x/"), vals("if(a)/x/.test(b)"))
        self.assertIn(("re", "/[/]/"), vals("return /[/]/.test(s)"))
        self.assertIn(("re", "/}/"), vals("{}/}/.exec(z)"))

    def test_templates_and_misc(self):
        toks = vals("`a${b+`c${d}e`}f`+g")
        self.assertEqual(toks[0], ("tpl", "`a${"))
        self.assertIn(("tpl", "`c${"), toks)
        self.assertEqual(toks[-3], ("tpl", "}f`"))
        self.assertIn(("id", "#priv"), vals("this.#priv=1"))
        self.assertEqual([v for _, v in vals("a?.5:b")], ["a", "?", ".5", ":", "b"])
        self.assertEqual(vals("1..toString()")[0], ("num", "1."))
        self.assertEqual(vals("#!/usr/bin/env node\nx")[0][0], "c")
        for bad in ("'abc", "a={", "x=/abc", "`a${b", "a)"):
            with self.assertRaises(FormatError, msg=bad):
                tokenize_js(bad)

    def test_format_keeps_tokens_and_newlines(self):
        src = "function f(){return\nx}var a={b:1,c:function(){for(;;){break}}};a.b++\n++c;x=`${{a:1}.a}`"
        out, _, n = format_js(src)
        self.assertEqual(vals(src), vals(out))
        self.assertIn("return\n", out)  # a quebra original (ASI) mantem-se
        self.assertIn("for(;;)", out)  # sem quebras dentro do cabecalho do for
        self.assertEqual(n, len(tokenize_js(src)))
        out2, _ = format_tokens(tokenize_js("a={x:1},b=function(){},c=2"))
        self.assertIn("},\n", out2)

    def test_minified_heuristic_and_css(self):
        self.assertFalse(is_minified("var a=1;\nvar b=2;\n"))
        self.assertTrue(is_minified("var a=1;" * 400))
        css = '@media (max-width:10px){.a{color:red;background:url(x;y.png)}}.b:hover{content:"};{"}'
        out, n = format_css(css)
        self.assertEqual([t.value for t in tokenize_css(css)], [t.value for t in tokenize_css(out)])
        self.assertIn("url(x;y.png)", out)
        self.assertIn('"};{"', out)
        with self.assertRaises(FormatError):
            format_css(".a{color:red")


class AnalysisTests(unittest.TestCase):
    BUNDLE = ('(()=>{var __webpack_modules__={184:e=>{e.exports={A:"a"}},22:(e,t,r)=>{"use strict";'
              'const v=R.views.lobby.Foo("x"),s=R.strings.menu.title;engine.call("PlaySound","x");'
              'engine.on("viewEnv.onDataChanged",f);t.d(t,{a:()=>c.createCallback(q,"onClose")});'
              'c.model.isOpen;viewEnv.getScale()}},__webpack_module_cache__={};'
              'var __webpack_exports__=__webpack_require__.O(void 0,[532],()=>__webpack_require__(22));})();')
    CHUNK = '(self.webpackChunkgameface=self.webpackChunkgameface||[]).push([[532],{7:e=>{e.exports=1},"x1":e=>{}}]);'

    def test_webpack_and_references(self):
        toks = tokenize_js(self.BUNDLE)
        info, mods = webpack_info(toks, self.BUNDLE)
        self.assertEqual((info["entry_module"], info["requires_chunks"], info["modules"]), ("22", ["532"], 2))
        self.assertEqual(sorted(mods), ["184", "22"])
        refs = js_references(toks)
        self.assertEqual(refs["r_views"], ["lobby.Foo"])
        self.assertEqual(refs["r_other"], {"strings": 1})
        self.assertIn("call:PlaySound", refs["engine"])
        self.assertIn("on:viewEnv.onDataChanged", refs["engine"])
        self.assertEqual(refs["commands"], ["onClose"])
        self.assertIn("isOpen", refs["names"])
        self.assertIn("getScale", refs["viewEnv"])
        cinfo, cmods = webpack_info(tokenize_js(self.CHUNK), self.CHUNK)
        self.assertEqual((cinfo["chunk_name"], cinfo["chunk_ids"], sorted(cmods)), ("webpackChunkgameface", ["532"], ["7", "x1"]))

    def test_snake(self):
        self.assertEqual(snake("BarracksView"), "barracks_view")
        self.assertEqual(snake("Comp7BattleCard"), "comp7_battle_card")
        self.assertEqual(snake("HTMLView"), "html_view")

    def test_node_mismatch_drops_formatted_copy(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(tmp), ignore_errors=True))
        src = tmp / "a.js"
        src.write_text("var x={a:1};" * 300, encoding="utf-8")
        job = {"key": "res/a.js", "src": str(src), "out_dir": str(tmp / "out"), "kind": "js", "format": True,
               "node": "node"}
        with mock.patch.object(gf_analyze, "node_check", side_effect=[(1, "SyntaxError"), (0, "")]):
            r = gf_analyze.process_file(job)
        self.assertEqual(r["status"], "partial")
        self.assertIn("alterou a sintaxe", r["error"])
        self.assertFalse((tmp / "out" / gf_analyze.formatted_rel("res/a.js", "js")).exists())
        with mock.patch.object(gf_analyze, "node_check", side_effect=[(1, "x"), (1, "x")]):
            r = gf_analyze.process_file(job)
        self.assertEqual(r["status"], "success")
        self.assertIn("original tambem", r["verify"]["node"])


def _view_files(name: str, extra_js: str = "") -> dict:
    base = f"gui/gameface/_dist/production/lobby/{name}"
    js = (AnalysisTests.BUNDLE.replace("R.views.lobby.Foo", f"R.views.lobby.{name}")
          + extra_js + ";var pad=" + "[" + ",".join(str(i) for i in range(900)) + "];")
    css = ".a{color:red}" * 300
    html = ('<!doctype html><html><head><link href="../../../../styles/default.css" rel="stylesheet">'
            f'<script>/** @license React v16.6.1\n */var r=1;</script>'
            f'<script defer="defer" src="../../lib/lobby/vendors.js"></script>'
            f'<script defer="defer" src="../../lobby/{name}/{name}.js"></script></head><body></body></html>')
    return {f"{base}/{name}.js": js.encode(), f"{base}/{name}.css": css.encode(), f"{base}/{name}.html": html.encode()}


class EngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(self.tmp), ignore_errors=True))
        files = {}
        files.update(_view_files("Foo"))
        files["gui/gameface/_dist/production/lib/lobby/vendors.js"] = b"/*! lib */var v=1;"
        files["gui/gameface/_dist/production/chunks/lobby/abc.js"] = AnalysisTests.CHUNK.encode()
        files["gui/gameface/_dist/production/lobby/Bad/Bad.js"] = b"var s='" + b"x" * 3000
        files["gui/gameface/_dist/production/lobby/Bad/Bad.html"] = b"<html></html>"
        files["gui/gameface/styles/default.css"] = b".x{}"
        files["gui/gameface/fonts/a.ttf"] = b"\x00\x01"
        files["gui/unbound/views/lobby/panel.unbound"] = b"(def macro Panel()\n (scope (var isOpen:bool = false)))"
        files["gui/gen_resources/gameface_layouts.json"] = json.dumps([
            {"type": "Layout", "id": "R.views.lobby.Foo",
             "path": "coui://gui/gameface/_dist/production/lobby/Foo/Foo.html",
             "parameters": {"entrance": "Foo", "impl": "gameface"}},
            {"type": "Layout", "id": "R.views.lobby.Demo", "path": "coui://gui/gameface/_dist/production/lobby/Demo/Demo.html",
             "parameters": {"entrance": "Demo", "impl": "gameface"}}]).encode()
        files["gui/gen_resources/unbound_layouts.json"] = json.dumps([
            {"type": "Layout", "id": "R.views.lobby.panel.Panel", "path": "gui/unbound/views/lobby/panel.unbound",
             "parameters": {"entrance": "Panel", "impl": "unbound"}}]).encode()
        files["scripts/client/gui/impl/lobby/foo_view.py"] = (
            b"class FooView(ViewImpl):\n    def __init__(self):\n"
            b"        settings = ViewSettings(R.views.lobby.Foo(), model=FooViewModel())\n")
        files["scripts/client/gui/impl/gen/view_models/views/lobby/foo_view_model.py"] = (
            b"class FooViewModel(ViewModel):\n    def _initialize(self):\n"
            b"        self._addBoolProperty('isOpen', False)\n        self._addNumberProperty('count', 0)\n"
            b"        self.onClose = self._addCommand('onClose')\n")
        self.pkgs = {"gui-part1.pkg": files}
        self.cfg = load_config(project_root=self.tmp)
        self.cfg.output_root = self.tmp / "out"
        self.out = self.cfg.realm_output_dir("EU")

    def _extract(self, pkgs=None, prune=False, wotmods=None):
        root = make_install(self.tmp / "game", pkgs=pkgs or self.pkgs, wotmods=wotmods)
        return run_extract(self.cfg, inspect_install(root, ["cli"], deep=False), ExtractOptions(jobs=2, prune=prune))

    def _run(self, **kw):
        kw.setdefault("jobs", 2)
        node, label = find_node()
        return run_gameface(self.cfg, "EU", GFOptions(**kw), node=node, node_label=label)

    def _entries(self):
        return json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))["entries"]

    def test_requires_manifest(self):
        with self.assertRaises(ManifestError):
            self._run()

    def test_cycle(self):
        self._extract(wotmods={"me.mod.wotmod": {"res/gui/gameface/_dist/production/lobby/Foo/Foo.js":
                                                  _view_files("Foo", "var mod=1")[
                                                      "gui/gameface/_dist/production/lobby/Foo/Foo.js"]}})
        r = self._run()
        self.assertEqual(r.totals.get("failed", 0), 0, r.problems)
        e = self._entries()
        foo = e["res/gui/gameface/_dist/production/lobby/Foo/Foo.js"]["gameface"]
        self.assertEqual((foo["status"], foo["kind"], foo["minified"]), ("success", "js", True))
        fmt = self.out / foo["formatted"]
        text = fmt.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("/* wot-extractor: JavaScript FORMATADO"))
        self.assertIn("NAO e o codigo-fonte original", text)
        css = e["res/gui/gameface/_dist/production/lobby/Foo/Foo.css"]["gameface"]
        self.assertTrue((self.out / css["formatted"]).is_file())
        bad = e["res/gui/gameface/_dist/production/lobby/Bad/Bad.js"]["gameface"]
        self.assertEqual(bad["status"], "partial")
        self.assertIn("lexer", bad["error"])
        self.assertNotIn("formatted", bad)
        self.assertNotIn("gameface", e["res/gui/gameface/fonts/a.ttf"])  # assets so indexados

        gf = self.out / "sources_gameface"
        view = json.loads((gf / "manifests/views/lobby.Foo.json").read_text(encoding="utf-8"))
        self.assertEqual(view["rid"], "R.views.lobby.Foo")
        self.assertIn("mapeamento oficial", view["rid_source"])
        js = next(f for f in view["files"] if f["name"] == "Foo.js")
        self.assertTrue(js["effective"].startswith("mods/"))  # o mod sobrepoe o ficheiro do jogo
        self.assertEqual(len(js["all"]), 2)
        deps = {d["virtual"] for d in view["dependencies"]}
        self.assertIn("gui/gameface/_dist/production/lib/lobby/vendors.js", deps)
        self.assertIn("gui/gameface/_dist/production/chunks/lobby/abc.js", deps)  # chunk 532 do webpack
        self.assertIn("gui/gameface/styles/default.css", deps)
        link = view["link"]
        self.assertEqual(link["confidence"], "provavel-forte", link)
        self.assertEqual(link["view_model"]["class"], "FooViewModel")
        self.assertEqual(link["view_model"]["coverage"]["missing"], ["count"])
        self.assertEqual(link["python_files"], ["sources/res/scripts/client/gui/impl/lobby/foo_view.py"])
        self.assertIn("call:PlaySound", view["engine"])
        panel = json.loads((gf / "manifests/views/lobby.panel.Panel.json").read_text(encoding="utf-8"))
        self.assertEqual(panel["impl"], "unbound")
        index = json.loads((gf / "manifests/index.json").read_text(encoding="utf-8"))
        self.assertEqual(index["layouts_without_files"], ["R.views.lobby.Demo"])
        self.assertIn("R.views.lobby.Bad", json.dumps(index["views"]))  # sem layout: id pela pasta
        self.assertFalse(index["views"]["lobby.Bad"]["official_id"])
        assets = json.loads((gf / "assets/index.json").read_text(encoding="utf-8"))
        self.assertEqual([a["key"] for a in assets["assets"]], ["res/gui/gameface/fonts/a.ttf"])
        md = (gf / "VIEWS.md").read_text(encoding="utf-8")
        self.assertIn("não é o código-fonte original", md)
        self.assertIn("`R.views.lobby.Bad` *", md)
        self.assertTrue((self.out / "gameface_report.json").is_file())

        r2 = self._run()
        self.assertEqual((r2.to_process, r2.pyindex_cached), (0, True))
        self.assertEqual(self._run(retry=True).to_process, 1)  # o Bad.js (partial)

        self._extract()  # extract incremental preserva o estado (o mod deixa de existir: prune nao pedido)
        self.assertIn("gameface", self._entries()["res/gui/gameface/_dist/production/lobby/Foo/Foo.js"])
        pkgs = {"gui-part1.pkg": dict(self.pkgs["gui-part1.pkg"])}
        del pkgs["gui-part1.pkg"]["gui/gameface/_dist/production/lobby/Foo/Foo.css"]
        self._extract(pkgs, prune=True)
        self.assertFalse((self.out / css["formatted"]).exists())
        self.assertFalse((self.out / css["analysis"]).exists())

    def test_dry_run_filters_and_no_format(self):
        self._extract()
        r = self._run(dry_run=True)
        self.assertEqual(r.to_process, r.selected)
        self.assertFalse((self.out / "sources_gameface/manifests/index.json").exists())
        self.assertEqual(self._run(globs=("*Foo.js",), dry_run=True).selected, 1)
        self._run(format=False, links=False)
        foo = self._entries()["res/gui/gameface/_dist/production/lobby/Foo/Foo.js"]["gameface"]
        self.assertNotIn("formatted", foo)
        view = json.loads((self.out / "sources_gameface/manifests/views/lobby.Foo.json").read_text(encoding="utf-8"))
        self.assertNotIn("link", view)


if __name__ == "__main__":
    unittest.main()
