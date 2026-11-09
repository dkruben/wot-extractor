# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/VehicleHealController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/VehicleHealController.py
from __future__ import absolute_import
import typing
from future.utils import viewvalues
from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent
from view_state_component import ViewStateComponentAdaptor

class VehicleHealController(DynamicScriptComponent):

    def __init__(self):
        super(VehicleHealController, self).__init__()
        self.__adaptors = {}

    def onDestroy(self):
        for adaptor in viewvalues(self.__adaptors):
            adaptor.destroy()

        self.__adaptors.clear()
        super(VehicleHealController, self).onDestroy()

    def set_displayedStates(self, prev):
        if self._isAvatarReady:
            self.__invalidateDisplayedStates()

    def _onAvatarReady(self):
        self.__invalidateDisplayedStates()

    def __invalidateDisplayedStates(self):
        removedStates = set(self.__adaptors)
        for stateDict in self.displayedStates:
            state = fixed_dict.getStateWithTimeInterval(stateDict)
            stateID = state.stateID
            if stateID in self.__adaptors:
                self.__adaptors[stateID].updateState(state)
                removedStates.remove(stateID)
            else:
                self.__adaptors[stateID] = ViewStateComponentAdaptor(entity=self.entity, state=state)

        for stateID in removedStates:
            adaptor = self.__adaptors.pop(stateID)
            adaptor.destroy()
