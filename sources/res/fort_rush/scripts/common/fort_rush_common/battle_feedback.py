# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/battle_feedback.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/battle_feedback.py
from __future__ import absolute_import

def packPersonalScoreFeedback(score, totalScore):
    return (score & 4294967295L) << 32 | totalScore & 4294967295L


def unpackPersonalScoreFeedback(packedData):
    score = packedData >> 32 & 4294967295L
    totalScore = packedData & 4294967295L
    return (score, totalScore)
