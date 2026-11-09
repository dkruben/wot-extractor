# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/abilities/equipment_tracking.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/abilities/equipment_tracking.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class EquipmentAnimatorTrigger(object):
    domain = CGF.Domain.ClientEditor
    activeTrigger = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='active trigger name')
    inactiveTrigger = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='inactive trigger name')


class EquipmentStateComponent(object):
    state = property((lambda self: self.__state))

    def __init__(self, state):
        self.__state = state


class EquipmentTrackerComponent(object):

    def __init__(self):
        self.__equipmentGameObjects = {}
        self.__reservedIDs = set()

    def reserveID(self, equipmentID):
        self.__reservedIDs.add(equipmentID)

    def isReserved(self, equipmentID):
        return equipmentID in self.__reservedIDs

    def startTrack(self, equipmentID, gameObject):
        self.__equipmentGameObjects[equipmentID] = gameObject

    def getEquipmentGameObject(self, equipmentID):
        return self.__equipmentGameObjects.get(equipmentID, None)
