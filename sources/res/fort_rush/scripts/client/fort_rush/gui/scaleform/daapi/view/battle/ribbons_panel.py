# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/ribbons_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/ribbons_panel.py
from __future__ import absolute_import
from fort_rush.gui.scaleform.daapi.view.battle import ribbons_aggregator
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_BATTLE_EFFICIENCY_TYPES import FORT_RUSH_BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from gui.impl import backport
from gui.impl.gen import R

class FortRushBattleRibbonsPanel(BattleRibbonsPanel):

    def __init__(self):
        super(FortRushBattleRibbonsPanel, self).__init__(ribbonsAggregator=ribbons_aggregator.createRibbonsAggregator())

    def _populate(self):
        super(FortRushBattleRibbonsPanel, self)._populate()
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onRespawnBaseMoving += self.__onRespawnBaseMoving
        return

    def _dispose(self):
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onRespawnBaseMoving -= self.__onRespawnBaseMoving
        super(FortRushBattleRibbonsPanel, self)._dispose()
        return

    def __onRespawnBaseMoving(self):
        self._ribbonsAggregator.clearRibbonsData()
        self.as_resetS()

    def _getRibbonsConfig(self):
        result = super(FortRushBattleRibbonsPanel, self)._getRibbonsConfig()
        result.extend([
         [
          FORT_RUSH_BATTLE_EFFICIENCY_TYPES.FORT_RUSH_BASE_CAPTURE_HEAL,
          backport.text(R.strings.fort_rush.battleEfficiency.baseHeal())],
         [
          FORT_RUSH_BATTLE_EFFICIENCY_TYPES.FORT_RUSH_POINTS,
          backport.text(R.strings.fort_rush.battleEfficiency.personalPoints())]])
        return result
