# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_itertools.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_itertools.py
from .. import fixer_base
from ..fixer_util import Name

class FixItertools(fixer_base.BaseFix):
    BM_compatible = True
    it_funcs = "('imap'|'ifilter'|'izip'|'izip_longest'|'ifilterfalse')"
    PATTERN = "\n              power< it='itertools'\n                  trailer<\n                     dot='.' func=%(it_funcs)s > trailer< '(' [any] ')' > >\n              |\n              power< func=%(it_funcs)s trailer< '(' [any] ')' > >\n              " % locals()
    run_order = 6

    def transform(self, node, results):
        prefix = None
        func = results['func'][0]
        if 'it' in results and func.value not in (u'ifilterfalse', u'izip_longest'):
            dot, it = results['dot'], results['it']
            prefix = it.prefix
            it.remove()
            dot.remove()
            func.parent.replace(func)
        prefix = prefix or func.prefix
        func.replace(Name(func.value[1:], prefix=prefix))
        return
