# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tooltips/battle_efficiency_tooltips_views.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tooltips/battle_efficiency_tooltips_views.py
from frameworks.wulf import ViewSettings
from gui.battle_results.presenters.packers.tooltips.efficiency_tooltips import CriticalDamageTooltipPacker
from gui.battle_results.presenters.wrappers import hasPresenter
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.critical_damage_tooltip_model import CriticalDamageTooltipModel
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel
from gui.impl.gen import R
from gui.impl.lobby.battle_results.tooltips_packers import BattleEfficiencyTooltipsPacker
from gui.impl.pub import ViewImpl

class BattleResultsStatsTooltipView(ViewImpl):
    _TOOLTIPS_PACKER = BattleEfficiencyTooltipsPacker

    def __init__(self, arenaUniqueID, paramType, userName):
        settings = ViewSettings(layoutID=R.views.lobby.tooltips.BattleResultsStatsTooltipView(), model=EfficiencyTooltipModel())
        super(BattleResultsStatsTooltipView, self).__init__(settings)
        self.__efficiencyParam = paramType
        self.__arenaUniqueID = arenaUniqueID
        self.__userName = userName

    @property
    def arenaUniqueID(self):
        return self.__arenaUniqueID

    def _onLoading(self, *args, **kwargs):
        super(BattleResultsStatsTooltipView, self)._onLoading(*args, **kwargs)
        self.__packContent()

    @hasPresenter()
    def __packContent(self, presenter=None):
        battleResults = presenter.getResults()
        with self.getViewModel().transaction() as model:
            self._TOOLTIPS_PACKER.packTooltip(model, battleResults, ctx={'paramType': (self.__efficiencyParam), 'userName': (self.__userName), 'isZeroValuesVisible': False, 
               'isAdditionalValuesVisible': True})


class BattleResultsCriticalDamageTooltipView(ViewImpl):

    def __init__(self, arenaUniqueID, paramType, userName):
        settings = ViewSettings(layoutID=R.views.mono.post_battle.tooltips.critical_damage(), model=CriticalDamageTooltipModel())
        super(BattleResultsCriticalDamageTooltipView, self).__init__(settings)
        self.__efficiencyParam = paramType
        self.__arenaUniqueID = arenaUniqueID
        self.__userName = userName

    @property
    def arenaUniqueID(self):
        return self.__arenaUniqueID

    def _onLoading(self, *args, **kwargs):
        super(BattleResultsCriticalDamageTooltipView, self)._onLoading(*args, **kwargs)
        self.__packContent()

    @hasPresenter()
    def __packContent(self, presenter=None):
        battleResults = presenter.getResults()
        with self.getViewModel().transaction() as model:
            CriticalDamageTooltipPacker.packTooltip(model, battleResults, ctx={'paramType': (self.__efficiencyParam), 'userName': (self.__userName), 'isZeroValuesVisible': False, 
               'isAdditionalValuesVisible': True})
