# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMReconAbilityEntityComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMReconAbilityEntityComponent.py
from __future__ import absolute_import
import typing
from Event import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent

class SMReconAbilityEntityComponent(DynamicScriptComponent):
    onSMReconEntityCreated = Event()
    onSMReconAbilitySpottedVehicles = Event()

    def __init__(self):
        super(SMReconAbilityEntityComponent, self).__init__()
        self.onSMReconEntityCreated(self.entity.id)

    def set_spottedVehiclesIDs(self, prevValues):
        if any(vehId not in set(prevValues) for vehId in self.spottedVehiclesIDs):
            self.onSMReconAbilitySpottedVehicles(self.spottedVehiclesIDs)
