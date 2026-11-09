# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/formatters/numbers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/numbers.py
from __future__ import absolute_import
from typing import Optional, Callable
from gui.impl import backport

def formatInt(value, negativeOrZero=None, formatter=backport.getIntegralFormat):
    if value <= 0 and negativeOrZero is not None:
        result = negativeOrZero
    else:
        result = formatter(value)
    return result


def makeStringWithThousandSymbol(value, digitLimit=4, formatter=backport.getIntegralFormat):
    limitValue = 10 ** digitLimit - 1
    if value > limitValue:
        result = formatter(int(value * 0.001)) + 'K'
    else:
        result = formatInt(value, '-', formatter)
    return result
