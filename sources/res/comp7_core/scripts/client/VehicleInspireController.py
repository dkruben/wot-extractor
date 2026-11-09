# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/VehicleInspireController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/VehicleInspireController.py
from __future__ import absolute_import
import typing
from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent
from view_state_component import ViewStateComponentAdaptor

class VehicleInspireController(DynamicScriptComponent):

    def __init__(self):
        super(VehicleInspireController, self).__init__()
        self.__adaptor = None
        return

    def onDestroy(self):
        if self.__adaptor is not None:
            self.__adaptor.destroy()
            self.__adaptor = None
        super(VehicleInspireController, self).onDestroy()
        return

    def set_isActive(self, prev):
        if self._isAvatarReady:
            self.__invalidateDisplayedState()

    def set_displayedState(self, prev):
        if self._isAvatarReady:
            self.__invalidateDisplayedState()

    def _onAvatarReady(self):
        self.__invalidateDisplayedState()

    def __invalidateDisplayedState(self):
        if self.isActive:
            state = fixed_dict.getStateWithTimeInterval(self.displayedState)
            if self.__adaptor is not None:
                self.__adaptor.updateState(state)
            else:
                self.__adaptor = ViewStateComponentAdaptor(entity=self.entity, state=state)
        elif self.__adaptor is not None:
            self.__adaptor.destroy()
            self.__adaptor = None
        return
