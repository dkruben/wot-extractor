# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/level_reserves_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/tooltips/level_reserves_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewFlags, ViewSettings
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.level_reserves_tooltip_model import LevelReservesTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class LevelReservesTooltip(ViewImpl):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self):
        settings = ViewSettings(R.views.frontline.mono.lobby.tooltips.level_reserves_tooltip(), ViewFlags.VIEW, LevelReservesTooltipModel())
        super(LevelReservesTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LevelReservesTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(LevelReservesTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as vm:
            levels = vm.getLevels()
            levels.clear()
            for level in self.__epicController.getSkillLevelRanks():
                levels.addString(level)

            levels.invalidate()
            vm.setHasOptionalReserves(True)
