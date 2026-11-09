# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_sys_exc.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_sys_exc.py
from .. import fixer_base
from ..fixer_util import Attr, Call, Name, Number, Subscript, Node, syms

class FixSysExc(fixer_base.BaseFix):
    exc_info = [
     u'exc_type', u'exc_value', u'exc_traceback']
    BM_compatible = True
    PATTERN = "\n              power< 'sys' trailer< dot='.' attribute=(%s) > >\n              " % ('|').join("'%s'" % e for e in exc_info)

    def transform(self, node, results):
        sys_attr = results['attribute'][0]
        index = Number(self.exc_info.index(sys_attr.value))
        call = Call(Name(u'exc_info'), prefix=sys_attr.prefix)
        attr = Attr(Name(u'sys'), call)
        attr[1].children[0].prefix = results['dot'].prefix
        attr.append(Subscript(index))
        return Node(syms.power, attr, prefix=node.prefix)
