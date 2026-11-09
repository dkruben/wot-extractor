# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWBuffPanelComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWBuffPanelComponent.py
from __future__ import absolute_import
import BigWorld
from dyn_components_groups import groupComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider
from xml_config_specs import StrParam
from constants import ARENA_BONUS_TYPE_IDS

@groupComponent(buffKey=StrParam(), showNotificationPopup=StrParam())
class HWBuffPanelComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(HWBuffPanelComponent, self).__init__()
        self._buffKey = self.groupComponentConfig.buffKey
        self._showNotificationPopup = self.groupComponentConfig.showNotificationPopup.split()

    @property
    def buffKey(self):
        return self._buffKey

    def _onAvatarReady(self):
        super(HWBuffPanelComponent, self)._onAvatarReady()
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        arenaBonusType = BigWorld.player().arena.bonusType
        if hwBattleGuiCtrl:
            ctx = {'buffKey': (self.buffKey), 'vehicleID': (self.entity.id), 
               'showNotificationPopup': (ARENA_BONUS_TYPE_IDS[arenaBonusType] in self._showNotificationPopup)}
            hwBattleGuiCtrl.applyBuff(ctx)

    def onDestroy(self):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.unapplyBuff({'buffKey': (self.buffKey), 
               'vehicleID': (self.entity.id)})
        super(HWBuffPanelComponent, self).onDestroy()
