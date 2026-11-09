# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_itertools_imports.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_itertools_imports.py
from lib2to3 import fixer_base
from lib2to3.fixer_util import BlankLine, syms, token

class FixItertoolsImports(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              import_from< 'from' 'itertools' 'import' imports=any >\n              " % locals()

    def transform(self, node, results):
        imports = results['imports']
        if imports.type == syms.import_as_name or not imports.children:
            children = [
             imports]
        else:
            children = imports.children
        for child in children[::2]:
            if child.type == token.NAME:
                member = child.value
                name_node = child
            elif child.type == token.STAR:
                return
            name_node = child.children[0]
            member_name = name_node.value
            if member_name in (u'imap', u'izip', u'ifilter'):
                child.value = None
                child.remove()
            elif member_name in (u'ifilterfalse', u'izip_longest'):
                node.changed()
                name_node.value = u'filterfalse' if member_name[1] == u'f' else u'zip_longest'

        children = imports.children[:] or [imports]
        remove_comma = True
        for child in children:
            if remove_comma and child.type == token.COMMA:
                child.remove()
            else:
                remove_comma ^= True

        while children and children[-1].type == token.COMMA:
            children.pop().remove()

        if not (imports.children or getattr(imports, 'value', None)) or imports.parent is None:
            p = node.prefix
            node = BlankLine()
            node.prefix = p
            return node
        else:
            return
