# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_execfile.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_execfile.py
from .. import fixer_base
from ..fixer_util import Comma, Name, Call, LParen, RParen, Dot, Node, ArgList, String, syms

class FixExecfile(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< 'execfile' trailer< '(' arglist< filename=any [',' globals=any [',' locals=any ] ] > ')' > >\n    |\n    power< 'execfile' trailer< '(' filename=any ')' > >\n    "

    def transform(self, node, results):
        filename = results['filename']
        globals = results.get('globals')
        locals = results.get('locals')
        execfile_paren = node.children[-1].children[-1].clone()
        open_args = ArgList([filename.clone(), Comma(), String('"rb"', ' ')], rparen=execfile_paren)
        open_call = Node(syms.power, [Name(u'open'), open_args])
        read = [Node(syms.trailer, [Dot(), Name(u'read')]),
         Node(syms.trailer, [LParen(), RParen()])]
        open_expr = [open_call] + read
        filename_arg = filename.clone()
        filename_arg.prefix = u' '
        exec_str = String(u"'exec'", u' ')
        compile_args = open_expr + [Comma(), filename_arg, Comma(), exec_str]
        compile_call = Call(Name(u'compile'), compile_args, u'')
        args = [
         compile_call]
        if globals is not None:
            args.extend([Comma(), globals.clone()])
        if locals is not None:
            args.extend([Comma(), locals.clone()])
        return Call(Name(u'exec'), args, prefix=node.prefix)
