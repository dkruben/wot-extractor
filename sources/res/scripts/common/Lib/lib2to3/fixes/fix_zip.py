# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_zip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_zip.py
from .. import fixer_base
from ..fixer_util import Name, Call, in_special_context

class FixZip(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = "\n    power< 'zip' args=trailer< '(' [any] ')' >\n    >\n    "
    skip_on = 'future_builtins.zip'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        else:
            if in_special_context(node):
                return None
            new = node.clone()
            new.prefix = u''
            new = Call(Name(u'list'), [new])
            new.prefix = node.prefix
            return new
