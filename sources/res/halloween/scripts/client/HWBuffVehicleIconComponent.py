# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWBuffVehicleIconComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWBuffVehicleIconComponent.py
from __future__ import absolute_import
from dyn_components_groups import groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent
from xml_config_specs import StrParam, IntParam
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import dependency
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID

@groupComponent(icon=StrParam(), priority=IntParam(default=1))
class HWBuffVehicleIconComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(HWBuffVehicleIconComponent, self).__init__()
        self._icon = self.groupComponentConfig.icon
        self._priority = self.groupComponentConfig.priority

    def _onAvatarReady(self):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.addVehicleMarkerIcon(self.entity.id, self._icon, self._priority)

    def onDestroy(self):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.removeVehicleMarkerIcon(self.entity.id, self._icon, self._priority)
        super(HWBuffVehicleIconComponent, self).onDestroy()

    @property
    def icon(self):
        return self._icon
