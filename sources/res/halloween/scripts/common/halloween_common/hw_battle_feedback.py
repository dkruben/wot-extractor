# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/common/halloween_common/hw_battle_feedback.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/common/halloween_common/hw_battle_feedback.py
from __future__ import absolute_import
from collections import namedtuple
HWGameplayAction = namedtuple('HWGameplayAction', ('value', 'targetID', 'id'))

class HWGameplayActionID(object):
    UNKNOWN = 0
    VEHICLE_REPAIR_INCOMING = 1
    VEHICLE_REPAIR_OUTCOMING = 2
    MODULES_DAMAGE_BLOCKED = 3
    HEALTH_DRAINED_BY_PASSIVE_VAMPIRE = 4
    SHELLS_LOOT_PICKUP = 5
    HANGAR_ITEMS_LOOT_PICKUP = 6
    HANGAR_ITEMS_LOOT_RECEIVE = 7
    SOULS_LOOT_PICKUP = 8
    SHELLS_LOOT_RECEIVE = 9
    SOULS_LOOT_RECEIVE = 10
    ANOMALY_LOOT_PICKUP = 11
    ANOMALY_LOOT_RECEIVE = 12
    SOULS_LOOT_REFUND = 13
    BOMBER_RESIST = 14
    SOULS_MIRIUMIZATION_ADD = 15
    SOULS_MIRIUMIZATION_DECREASE = 16


def packGameplayActionFeedback(action):
    return (int(action.targetID) & 4294967295L) << 32 | (int(action.value) & 65535) << 16 | action.id & 65535


def unpackGameplayActionFeedback(packedData):
    return HWGameplayAction(targetID=packedData >> 32 & 4294967295L, value=packedData >> 16 & 65535, id=packedData & 65535)
