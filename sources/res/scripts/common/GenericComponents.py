# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/GenericComponents.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/GenericComponents.py
from __future__ import absolute_import
import enum
COMPOSITION_ROOT_SLOT_NAME = 'compositionRootSlot'

class EHealthGradation(enum.Enum):
    RED_ZONE = 'RED_ZONE'
    YELLOW_ZONE = 'YELLOW_ZONE'
    GREEN_ZONE = 'GREEN_ZONE'


class HealthGradationComponent:

    def __init__(self, redHealth, yellowHealth):
        self.__redHealth = redHealth
        self.__yellowHealth = yellowHealth

    def getHealthZone(self, health, maxHealth):
        if health < maxHealth * self.__redHealth // 100:
            return EHealthGradation.RED_ZONE
        if health < maxHealth * self.__yellowHealth // 100:
            return EHealthGradation.YELLOW_ZONE
        return EHealthGradation.GREEN_ZONE


class CyclicActivatorComponent(object):
    pass


class VSEComponent(object):
    pass


class StateSwitcherComponent(object):
    NONE_STATE = 0
    NORMAL_STATE = 1
    DAMAGED_STATE = 2
    CRITICAL_STATE = 3
