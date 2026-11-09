# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_raise.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_raise.py
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, Attr, ArgList, is_tuple

class FixRaise(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    raise_stmt< 'raise' exc=any [',' val=any [',' tb=any]] >\n    "

    def transform(self, node, results):
        syms = self.syms
        exc = results['exc'].clone()
        if exc.type == token.STRING:
            msg = 'Python 3 does not support string exceptions'
            self.cannot_convert(node, msg)
            return
        else:
            if is_tuple(exc):
                while is_tuple(exc):
                    exc = exc.children[1].children[0].clone()

                exc.prefix = u' '
            if 'val' not in results:
                new = pytree.Node(syms.raise_stmt, [Name(u'raise'), exc])
                new.prefix = node.prefix
                return new
            val = results['val'].clone()
            if is_tuple(val):
                args = [c.clone() for c in val.children[1:-1]]
            else:
                val.prefix = u''
                args = [val]
            if 'tb' in results:
                tb = results['tb'].clone()
                tb.prefix = u''
                e = exc
                if val.type != token.NAME or val.value != u'None':
                    e = Call(exc, args)
                with_tb = Attr(e, Name(u'with_traceback')) + [ArgList([tb])]
                new = pytree.Node(syms.simple_stmt, [Name(u'raise')] + with_tb)
                new.prefix = node.prefix
                return new
            return pytree.Node(syms.raise_stmt, [
             Name(u'raise'), Call(exc, args)], prefix=node.prefix)
