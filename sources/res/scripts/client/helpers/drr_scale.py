# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/drr_scale.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/drr_scale.py
from __future__ import absolute_import, division
import BigWorld
from math_common import decimal_round
DRR_MIN_SCALE_VALUE = 0.6
DRR_MAX_SCALE_VALUE = 1.0
DRR_MAX_STEP_VALUE = 0.05
DRR_EPSILON_VALUE = DRR_MAX_STEP_VALUE - 0.01
PERCENT_MODIFIER = 100.0

def normalizeScale(value):
    result = min(max(decimal_round(value, 2), DRR_MIN_SCALE_VALUE), DRR_MAX_SCALE_VALUE)
    modulo = result * PERCENT_MODIFIER % (DRR_MAX_STEP_VALUE * PERCENT_MODIFIER)
    if modulo:
        result = result - modulo / PERCENT_MODIFIER
    return result


def getPercent(value):
    return decimal_round(value, 3) * PERCENT_MODIFIER


def changeScaleByStep(offset):
    result = None
    scale = BigWorld.getDRRScale()
    newScale = normalizeScale(scale + offset)
    if abs(scale - newScale) >= DRR_EPSILON_VALUE:
        BigWorld.setDRRScale(newScale)
        if normalizeScale(BigWorld.getDRRScale()) == newScale:
            result = newScale
    return result


def stepUp():
    return changeScaleByStep(DRR_MAX_STEP_VALUE)


def stepDown():
    return changeScaleByStep(-DRR_MAX_STEP_VALUE)
