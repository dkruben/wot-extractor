# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/formatters.py
from __future__ import absolute_import, division
import math
from debug_utils import LOG_ERROR, LOG_WARNING

def normalizeHealth(health):
    return max(0.0, health)


def getHealthPercent(health, maxHealth):
    if not (maxHealth > 0 and maxHealth >= health):
        LOG_WARNING(('Maximum health is not valid! health={}, maxHealth={}').format(health, maxHealth))
        return 0.0
    return float(normalizeHealth(health)) / maxHealth


def normalizeHealthPercent(health, maxHealth):
    return int(math.ceil(getHealthPercent(health, maxHealth) * 100))


def formatHealthProgress(health, maxHealth):
    if not (maxHealth > 0 and maxHealth >= health):
        LOG_ERROR(('Maximum health is not valid! health={}, maxHealth={}').format(health, maxHealth))
    return '%d/%d' % (normalizeHealth(health), maxHealth)
