# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_numliterals.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_numliterals.py
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Number

class FixNumliterals(fixer_base.BaseFix):
    _accept_type = token.NUMBER

    def match(self, node):
        return node.value.startswith(u'0') or node.value[-1] in u'Ll'

    def transform(self, node, results):
        val = node.value
        if val[-1] in u'Ll':
            val = val[:-1]
        elif val.startswith(u'0') and val.isdigit() and len(set(val)) > 1:
            val = u'0o' + val[1:]
        return Number(val, prefix=node.prefix)
