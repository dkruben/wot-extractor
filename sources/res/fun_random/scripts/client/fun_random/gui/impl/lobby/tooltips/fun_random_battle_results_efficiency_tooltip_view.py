# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_battle_results_efficiency_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_battle_results_efficiency_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService

class PersonalEfficiencyParamTooltip(ViewImpl):
    __battleResults = dependency.descriptor(IBattleResultsService)

    def __init__(self, arenaUniqueID, paramType, packer):
        settings = ViewSettings(layoutID=R.views.lobby.tooltips.BattleResultsStatsTooltipView(), model=EfficiencyTooltipModel())
        super(PersonalEfficiencyParamTooltip, self).__init__(settings)
        self.__efficiencyParam = paramType
        self.__arenaUniqueID = arenaUniqueID
        self.__packer = packer

    @property
    def arenaUniqueID(self):
        return self.__arenaUniqueID

    def _onLoading(self, *args, **kwargs):
        super(PersonalEfficiencyParamTooltip, self)._onLoading(*args, **kwargs)
        self.__invalidateAll()

    def _finalize(self):
        self.__packer = None
        super(PersonalEfficiencyParamTooltip, self)._finalize()
        return

    def __invalidateAll(self):
        statsCtrl = self.__battleResults.getStatsCtrl(self.arenaUniqueID)
        with self.getViewModel().transaction() as model:
            self.__packer.packTooltip(model, statsCtrl.getResults(), ctx={'paramType': (self.__efficiencyParam)})
