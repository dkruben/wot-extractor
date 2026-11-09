# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_long.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_long.py
from lib2to3 import fixer_base
from lib2to3.fixer_util import is_probably_builtin

class FixLong(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'long'"

    def transform(self, node, results):
        if is_probably_builtin(node):
            node.value = u'int'
            node.changed()
