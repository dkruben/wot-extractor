# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/day_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/day_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.day_tooltip_model import DayTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class DayTooltip(ViewImpl):
    __slots__ = ('__params', )

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.day_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = DayTooltipModel()
        super(DayTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(DayTooltip, self).getViewModel()

    def _onLoading(self):
        super(DayTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setIndex(self.__params['index'])
            vm.setIsQualification(self.__params['isQualification'])
            vm.setSeasonName(self.__params['seasonName'])
            vm.setDiff(self.__params['diff'])
            vm.setHasBattles(self.__params['hasBattles'])
            vm.setRatingPoints(self.__params['ratingPoints'])
            vm.setRankInactivityPenalty(self.__params['rankInactivityPenalty'])
            vm.setCurrentDayIndex(self.__params['currentDayIndex'])
            rank = self.__params['rank']
            if rank:
                vm.setRank(rank)
            division = self.__params['division']
            if division:
                vm.setDivision(division)
