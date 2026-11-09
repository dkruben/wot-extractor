# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/boss_indicator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/boss_indicator.py
from __future__ import absolute_import
from account_helpers.settings_core import settings_constants
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from halloween.gui.scaleform.daapi.view.meta.HWBossIndicatorProgressMeta import HWBossIndicatorProgressMeta
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider

class HWBossIndicator(HWBossIndicatorProgressMeta):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def _populate(self):
        super(HWBossIndicator, self)._populate()
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.onVehicleDetectorChangeDistance += self.__handleChangeDistance
        self.settingsCore.onSettingsChanged += self.__onSettingsChange
        self.as_setValueS(0)
        self.as_setIndicatorEnabledS(True)
        self.__updateAlpha()

    def _dispose(self):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.onVehicleDetectorChangeDistance -= self.__handleChangeDistance
        self.settingsCore.onSettingsChanged -= self.__onSettingsChange
        super(HWBossIndicator, self)._dispose()

    def __handleChangeDistance(self, ctx):
        self.as_setValueS(ctx.get('indicator', 0))

    def __onSettingsChange(self, diff):
        if settings_constants.GAME.MINIMAP_ALPHA in diff or settings_constants.GAME.MINIMAP_ALPHA_ENABLED in diff:
            self.__updateAlpha()

    def __updateAlpha(self):
        value = 0.0
        if self.settingsCore.getSetting(settings_constants.GAME.MINIMAP_ALPHA_ENABLED):
            value = int(self.settingsCore.getSetting(settings_constants.GAME.MINIMAP_ALPHA))
        self.as_setAlphaS(1 - value / 100.0)
