# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/status_notifications/frontline_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/status_notifications/frontline_helpers.py
from __future__ import absolute_import
from items import vehicles

def getEquipmentById(equipmentId):
    return vehicles.g_cache.equipments()[equipmentId]


def getSmokeDataByPredicate(smokeInfo, teamPredicate, postEffectPredicate):
    if smokeInfo is None or not teamPredicate or not postEffectPredicate:
        return (None, None)
    if teamPredicate(smokeInfo['team']) and postEffectPredicate(smokeInfo['expiring']):
        return (smokeInfo['endTime'], getEquipmentById(smokeInfo['equipmentID']))
    else:
        return (None, None)
