# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_battle_results_economic_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_battle_results_economic_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from fun_random.gui.battle_results.tooltips.earned_currency_tooltips import FunEarnedCurrencyTooltipsPacker
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_economic_tooltip_view_model import FunRandomEconomicTooltipViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService

class FunRandomBattleResultsEconomicTooltipView(ViewImpl):
    __battleResults = dependency.descriptor(IBattleResultsService)

    def __init__(self, arenaUniqueID, currencyType):
        settings = ViewSettings(layoutID=R.views.fun_random.mono.lobby.tooltips.battle_results_economic_tooltip(), model=FunRandomEconomicTooltipViewModel())
        super(FunRandomBattleResultsEconomicTooltipView, self).__init__(settings)
        self.__arenaUniqueID = arenaUniqueID
        self.__currencyType = currencyType

    @property
    def arenaUniqueID(self):
        return self.__arenaUniqueID

    @property
    def viewModel(self):
        return super(FunRandomBattleResultsEconomicTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(FunRandomBattleResultsEconomicTooltipView, self)._onLoading(*args, **kwargs)
        self.__invalidateAll()

    def __invalidateAll(self):
        statsCtrl = self.__battleResults.getStatsCtrl(self.arenaUniqueID)
        with self.viewModel.transaction() as model:
            FunEarnedCurrencyTooltipsPacker.packTooltip(model, statsCtrl.getResults(), ctx={'currencyType': (self.__currencyType)})
