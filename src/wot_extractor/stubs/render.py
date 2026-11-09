"""Escrita dos stubs .pyi a partir das descricoes do worker (_describe27.py).

Regra: so o que foi verificado no codigo entra no stub: nomes de modulos/classes/funcoes, parametros (nomes,
*args, **kwargs, valores por omissao literais), bases, decoradores conhecidos, docstrings, atributos
atribuidos e o tipo de valores literais. Nada e anotado com tipos que o codigo nao mostra: o que nao se sabe
fica `Any` (desconhecido). Cada stub e validado pelo parser do Python 3.
"""

from __future__ import annotations

import ast
import keyword

RENDER_VERSION = 1
KNOWN_DECORATORS = frozenset(("property", "staticmethod", "classmethod", "abstractmethod", "abc.abstractmethod",
                              "abc.abstractproperty", "abstractproperty"))
ACCESSORS = (".setter", ".getter", ".deleter")
LITERAL_KINDS = frozenset(("int", "float", "str", "bool", "tuple", "list", "dict", "set", "complex"))

HEADER = ("# wot-extractor: STUB (.pyi) gerado a partir de {source} ({how}).\n"
          "# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e\n"
          "# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.\n")
HOW = {"ast": "arvore sintatica do codigo descompilado/original",
       "bytecode": "BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao"}


def valid_name(name: str | None) -> bool:
    return bool(name) and name.isidentifier() and not keyword.iskeyword(name)


def _doc_lines(doc: str | None, indent: str) -> list[str]:
    if not doc:
        return []
    text = doc.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    if text.endswith('"'):
        text += " "
    lines = text.split("\n")
    if len(lines) == 1:
        return [f'{indent}"""{lines[0]}"""']
    return [f'{indent}"""{lines[0]}'] + [f"{indent}{x}" if x.strip() else "" for x in lines[1:]] + [f'{indent}"""']


class Renderer:
    def __init__(self, module: str, is_package: bool, exists, any_name: str = "Any"):
        self.module = module
        self.is_package = is_package
        self.exists = exists  # callable(nome do modulo) -> bool
        self.package = module if is_package else module.rpartition(".")[0]
        self.any = any_name
        self.omitted: list[str] = []
        self.uses_any = False
        self.n_classes = 0
        self.n_functions = 0

    def A(self) -> str:
        self.uses_any = True
        return self.any

    # ---------------------------------------------------------- imports
    def _implicit_relative(self, name: str, future: list[str]) -> bool:
        """Python 2: `import x` dentro de um pacote refere-se primeiro ao irmao `<pacote>.x`, se existir."""
        if "absolute_import" in future or not self.package:
            return False
        return self.exists(f"{self.package}.{name.split('.')[0]}")

    def imports(self, desc: dict, skip: set[str]) -> list[str]:
        out = []
        future = desc.get("future") or []
        for imp in desc.get("imports", []):
            if imp["kind"] == "import":
                name, asname = imp["name"], imp.get("asname")
                bound = asname or name.split(".")[0]
                if bound in skip or not all(valid_name(p) for p in name.split(".")) or (asname and not valid_name(asname)):
                    continue
                if self._implicit_relative(name, future):
                    head, _, rest = name.partition(".")
                    if rest and asname:
                        mod, _, last = name.rpartition(".")
                        out.append(f"from .{mod} import {last} as {asname}")
                    else:
                        out.append(f"from . import {head} as {asname or head}")
                elif asname:
                    out.append(f"import {name} as {asname}")
                elif "." in name:
                    out.append(f"import {name}")
                else:
                    out.append(f"import {name} as {name}")
            else:
                mod, level = imp.get("module") or "", imp.get("level") or 0
                if mod and not all(valid_name(p) for p in mod.split(".")):
                    continue
                if level == 0 and mod and self._implicit_relative(mod, future):
                    prefix = "." + mod
                else:
                    prefix = "." * level + mod
                if not prefix:
                    continue
                names = []
                for n, asn in imp["names"]:
                    if n == "*":
                        names = ["*"]
                        break
                    b = asn or n
                    if b in skip or not valid_name(n) or not valid_name(b):
                        continue
                    names.append(f"{n} as {b}")
                if names:
                    out.append(f"from {prefix} import {', '.join(names)}")
        return out

    # ---------------------------------------------------------- definicoes
    def _assign(self, a: dict, indent: str, local_names: set[str]) -> list[str]:
        n = a["name"]
        if not valid_name(n):
            self.omitted.append(f"atributo '{n}'")
            return []
        if a.get("value") is not None:
            return [f"{indent}{n} = {a['value']}"]
        alias = a.get("alias")
        if alias and alias.split(".")[0] in local_names and all(valid_name(p) for p in alias.split(".")):
            return [f"{indent}{n} = {alias}"]
        kind = a.get("kind")
        return [f"{indent}{n}: {kind if kind in LITERAL_KINDS else self.A()}"]

    def _params(self, fn: dict) -> str | None:
        parts = []
        for i, a in enumerate(fn["args"]):
            name = a.get("name")
            if name is None:  # tuplo desempacotado (Python 2): posicional anonimo
                name = f"__p{i}"
            elif not valid_name(name):
                return None
            if a.get("has_default"):
                parts.append(f"{name}={a.get('default') or '...'}")
            else:
                parts.append(name)
        for key, star in (("vararg", "*"), ("kwarg", "**")):
            v = fn.get(key)
            if v:
                if not valid_name(v):
                    return None
                parts.append(f"{star}{v}")
        return ", ".join(parts)

    def function(self, fn: dict, indent: str, accessor_ok: set[str]) -> list[str]:
        name = fn["name"]
        if not valid_name(name):
            self.omitted.append(f"funcao '{name}'")
            return []
        params = self._params(fn)
        if params is None:
            self.omitted.append(f"funcao '{name}' (parametro com nome reservado em Python 3)")
            return []
        lines = []
        for d in fn.get("decorators", []):
            if d in KNOWN_DECORATORS or (d.endswith(ACCESSORS) and d.rsplit(".", 1)[0] in accessor_ok):
                lines.append(f"{indent}@{d}")
            else:
                lines.append(f"{indent}# decorador original: @{d}")
        if any(a.get("default_unknown") for a in fn["args"]):
            lines.append(f"{indent}# gerado do bytecode: quais parametros tem valor por omissao e desconhecido")
        lines.append(f"{indent}def {name}({params}):")
        body = _doc_lines(fn.get("doc"), indent + "    ")
        lines += body + [f"{indent}    ..."]
        self.n_functions += 1
        return lines

    def _functions(self, fns: list[dict], indent: str) -> list[str]:
        """A ultima definicao com o mesmo nome prevalece; acessores de property ficam depois do getter."""
        order: list[dict] = []
        for fn in fns:
            is_accessor = any(d.endswith(ACCESSORS) for d in fn.get("decorators", []))
            if not is_accessor:
                order = [f for f in order if f["name"] != fn["name"]]
            order.append(fn)
        props = {f["name"] for f in order if "property" in f.get("decorators", [])}
        out = []
        for fn in order:
            out += self.function(fn, indent, props)
        return out

    def klass(self, c: dict, indent: str, local_names: set[str]) -> list[str]:
        name = c["name"]
        if not valid_name(name):
            self.omitted.append(f"classe '{name}'")
            return []
        lines = []
        bases = []
        for b in c.get("bases", []):
            if b.get("simple") and all(valid_name(p) for p in b["src"].split(".")):
                bases.append(b["src"])
            else:
                lines.append(f"{indent}# base nao representavel no stub: {b.get('src') or '<expressao>'}")
        mc = c.get("metaclass")
        if mc and all(valid_name(p) for p in mc.split(".")):
            bases.append(f"metaclass={mc}")
        if c.get("bases_unknown"):
            lines.append(f"{indent}# gerado do bytecode: classes base desconhecidas")
        for d in c.get("decorators", []):
            lines.append(f"{indent}# decorador original: @{d}")
        lines.append(f"{indent}class {name}({', '.join(bases)}):" if bases else f"{indent}class {name}:")
        inner = indent + "    "
        body = _doc_lines(c.get("doc"), inner)
        defined = {m["name"] for m in c.get("methods", [])} | {k["name"] for k in c.get("classes", [])}
        attrs = {}
        for a in c.get("attrs", []):  # o ultimo valor prevalece
            if a["name"] not in defined:
                attrs[a["name"]] = a
        for a in attrs.values():
            body += self._assign(a, inner, local_names | set(attrs))
        for n in c.get("instance_attrs", []):
            if n not in defined and n not in attrs and valid_name(n):
                body.append(f"{inner}{n}: {self.A()}")
        for k in c.get("classes", []):
            body += self.klass(k, inner, local_names)
        body += self._functions(c.get("methods", []), inner)
        if not body:
            body = [f"{inner}..."]
        self.n_classes += 1
        return lines + body

    # ---------------------------------------------------------- modulo
    def render(self, desc: dict, source: str) -> str:
        classes = {c["name"]: c for c in desc.get("classes", [])}
        functions = desc.get("functions", [])
        fnames = {f["name"] for f in functions}
        assigns = {}
        for a in desc.get("assigns", []):
            if a["name"] not in classes and a["name"] not in fnames:
                assigns[a["name"]] = a
        skip = set(assigns) | set(classes) | fnames  # definicoes locais prevalecem sobre imports
        imports = self.imports(desc, skip)
        imported = set()
        for line in imports:
            for part in line.split(" import ", 1)[-1].split(","):
                imported.add(part.strip().split(" as ")[-1].strip())
        local_names = set(classes) | fnames | set(assigns) | imported
        body: list[str] = []
        for a in assigns.values():
            body += self._assign(a, "", local_names)
        for c in classes.values():
            body.append("")
            body += self.klass(c, "", local_names)
        fn_lines = self._functions(functions, "")
        if fn_lines:
            body.append("")
            body += fn_lines
        if desc.get("mode") == "bytecode":
            body += ["", f"def __getattr__(name: str) -> {self.A()}: ...  # stub incompleto (gerado do bytecode)"]
        head = [HEADER.format(source=source, how=HOW.get(desc.get("mode"), desc.get("mode")))]
        head += _doc_lines(desc.get("doc"), "")
        if self.uses_any:
            head.append("from typing import Any" if self.any == "Any" else f"from typing import Any as {self.any}")
        head += imports
        if self.omitted:
            head.append("# omitido (nomes que nao sao identificadores validos em Python 3): "
                        + ", ".join(self.omitted[:20]) + (" ..." if len(self.omitted) > 20 else ""))
        return "\n".join(head + body) + "\n"


def render_module(desc: dict, module: str, is_package: bool, source: str, exists) -> tuple[str, dict]:
    names = {c["name"] for c in desc.get("classes", [])} | {f["name"] for f in desc.get("functions", [])} | \
        {a["name"] for a in desc.get("assigns", [])}
    for imp in desc.get("imports", []):
        if imp["kind"] == "import":
            names.add(imp.get("asname") or imp["name"].split(".")[0])
        else:
            names.update(asn or n for n, asn in imp["names"])
    r = Renderer(module, is_package, exists, any_name="_Any" if "Any" in names else "Any")
    text = r.render(desc, source)
    error = None
    try:
        ast.parse(text)
    except SyntaxError as exc:
        error = f"SyntaxError no stub: {exc.msg} (linha {exc.lineno})"
        # sem docstrings (a causa mais provavel), mantendo o resto
        for c in desc.get("classes", []):
            _strip_docs(c)
        for f in desc.get("functions", []):
            f["doc"] = None
        desc = dict(desc, doc=None)
        r = Renderer(module, is_package, exists, any_name=r.any)
        text = r.render(desc, source)
        try:
            ast.parse(text)
            error += " -> gerado sem docstrings"
        except SyntaxError as exc2:
            text = (HEADER.format(source=source, how="FALHOU a geracao") +
                    f"# {error}; {exc2.msg} (linha {exc2.lineno})\nfrom typing import Any\n"
                    "def __getattr__(name: str) -> Any: ...\n")
            return text, {"classes": 0, "functions": 0, "omitted": r.omitted, "error": error, "failed": True}
    return text, {"classes": r.n_classes, "functions": r.n_functions, "omitted": r.omitted, "error": error,
                  "failed": False}


def _strip_docs(c: dict) -> None:
    c["doc"] = None
    for m in c.get("methods", []):
        m["doc"] = None
    for k in c.get("classes", []):
        _strip_docs(k)


NATIVE_HEADER = ("# wot-extractor: STUB do modulo '{name}', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).\n"
                 "# So lista os membros que o codigo Python usa ({files} ficheiro(s)); assinaturas e tipos sao\n"
                 "# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.\n")


def render_native(name: str, members: dict, files: int) -> str:
    """members: {nome: {"uses": n, "calls": n, "min": a, "max": b, "kw": [...], "imported": n}}"""
    lines = [NATIVE_HEADER.format(name=name, files=files), "from typing import Any", ""]
    for m in sorted(members):
        if not valid_name(m):
            continue
        info = members[m]
        notes = []
        if info.get("calls"):
            rng = ""
            if info.get("min") is not None:
                rng = (f" com {info['min']} argumento(s) posicional(is)" if info["min"] == info["max"]
                       else f" com {info['min']}-{info['max']} argumentos posicionais")
            notes.append(f"chamado {info['calls']}x{rng}")
            if info.get("kw"):
                notes.append("keywords: " + ", ".join(sorted(info["kw"])[:8]))
        if info.get("uses", 0) - info.get("calls", 0) > 0:
            notes.append(f"usado sem chamada {info['uses'] - info.get('calls', 0)}x")
        if info.get("imported"):
            notes.append(f"importado com 'from {name} import' em {info['imported']} ficheiro(s)")
        comment = "  # " + "; ".join(notes) if notes else ""
        if info.get("calls"):
            lines.append(f"def {m}(*args: Any, **kwargs: Any) -> Any: ...{comment}")
        else:
            lines.append(f"{m}: Any{comment}")
    lines += ["", "def __getattr__(name: str) -> Any: ...  # outros membros nao observados"]
    text = "\n".join(lines) + "\n"
    ast.parse(text)
    return text
