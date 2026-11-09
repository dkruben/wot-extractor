# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_dict.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_dict.py
from .. import pytree
from .. import patcomp
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, LParen, RParen, ArgList, Dot
from .. import fixer_util
iter_exempt = fixer_util.consuming_calls | set(['iter'])

class FixDict(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< head=any+\n         trailer< '.' method=('keys'|'items'|'values'|\n                              'iterkeys'|'iteritems'|'itervalues'|\n                              'viewkeys'|'viewitems'|'viewvalues') >\n         parens=trailer< '(' ')' >\n         tail=any*\n    >\n    "

    def transform(self, node, results):
        head = results['head']
        method = results['method'][0]
        tail = results['tail']
        syms = self.syms
        method_name = method.value
        isiter = method_name.startswith(u'iter')
        isview = method_name.startswith(u'view')
        if isiter or isview:
            method_name = method_name[4:]
        head = [n.clone() for n in head]
        tail = [n.clone() for n in tail]
        special = not tail and self.in_special_context(node, isiter)
        args = head + [
         pytree.Node(syms.trailer, [
          Dot(),
          Name(method_name, prefix=method.prefix)]),
         results['parens'].clone()]
        new = pytree.Node(syms.power, args)
        if not (special or isview):
            new.prefix = u''
            new = Call(Name(u'iter' if isiter else u'list'), [new])
        if tail:
            new = pytree.Node(syms.power, [new] + tail)
        new.prefix = node.prefix
        return new

    P1 = "power< func=NAME trailer< '(' node=any ')' > any* >"
    p1 = patcomp.compile_pattern(P1)
    P2 = "for_stmt< 'for' any 'in' node=any ':' any* >\n            | comp_for< 'for' any 'in' node=any any* >\n         "
    p2 = patcomp.compile_pattern(P2)

    def in_special_context(self, node, isiter):
        if node.parent is None:
            return False
        else:
            results = {}
            if node.parent.parent is not None and self.p1.match(node.parent.parent, results):
                if results['node'] is node:
                    if isiter:
                        return results['func'].value in iter_exempt
                    return results['func'].value in fixer_util.consuming_calls
            if not isiter:
                return False
            return self.p2.match(node.parent, results) and results['node'] is node
