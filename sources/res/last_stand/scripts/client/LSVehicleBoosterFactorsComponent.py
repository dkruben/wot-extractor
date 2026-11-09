# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSVehicleBoosterFactorsComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSVehicleBoosterFactorsComponent.py
from __future__ import absolute_import
from helpers import dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID
from last_stand_common.ls_utils.boosters import applyBoosterFactors, getFactorsDiff
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class LSVehicleBoosterFactorsComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    @property
    def lsBattleGuiCtrl(self):
        return self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.LS_BATTLE_GUI_CTRL)

    def set_factors(self, prev):
        diff = getFactorsDiff(self.factors or {}, prev or {})
        if diff:
            self.lsBattleGuiCtrl.onFactorsReady(self.entity.id, diff)

    def applyFactors(self, value, factorName):
        return applyBoosterFactors(value, factorName, self.factors or {})

    def _onAvatarReady(self):
        super(LSVehicleBoosterFactorsComponent, self)._onAvatarReady()
        if self.factors:
            self.lsBattleGuiCtrl.onFactorsReady(self.entity.id, set(self.factors.keys()))
