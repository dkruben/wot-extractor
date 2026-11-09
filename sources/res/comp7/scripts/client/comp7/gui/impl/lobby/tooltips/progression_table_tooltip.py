# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/progression_table_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/progression_table_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.progression_table_tooltip_model import ProgressionTableTooltipModel
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers, comp7_shared
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from comp7.gui.impl.lobby.meta_view import meta_view_helper
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class ProgressionTableTooltip(ViewImpl):
    __slots__ = ()
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.progression_table_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = ProgressionTableTooltipModel()
        super(ProgressionTableTooltip, self).__init__(settings)

    def _onLoading(self, *args, **kwargs):
        super(ProgressionTableTooltip, self)._onLoading(*args, **kwargs)
        self.__updateTooltipProgressionData()

    @property
    def viewModel(self):
        return super(ProgressionTableTooltip, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.__comp7Controller.onRankUpdated, self.__updateTooltipProgressionData),
         (
          self.__comp7Controller.onModeConfigChanged, self.__updateTooltipProgressionData),
         (
          self.__comp7Controller.onComp7RanksConfigChanged, self.__updateTooltipProgressionData))

    def __updateTooltipProgressionData(self, *_):
        playerDivision = comp7_shared.getPlayerDivision()
        rank = comp7_shared.getRankEnumValue(playerDivision)
        divisionByRank = comp7_shared.getPlayerDivisionByRankAndIndex(rank, playerDivision.index)
        ranksConfig = self.__comp7Controller.getRanksConfig()
        with self.viewModel.transaction() as vm:
            vm.setSeasonName(getSeasonNameEnum(self.__comp7Controller, SeasonName))
            vm.setCurrentScore(self.__comp7Controller.rating)
            vm.setCurrentItemIndex(ranksConfig.ranksOrder.index(rank))
            vm.setRankInactivityCount(self.__comp7Controller.activityPoints)
            vm.setRankInactivityPointsCount(divisionByRank.ratingPointsPenalty)
            vm.setEarnedRankInactivityPerBattle(divisionByRank.activityPointsPerBattle)
            comp7_model_helpers.setElitePercentage(vm)
            self.__setupRanksTable(vm)

    def __setupRanksTable(self, viewModel):
        ranksConfig = self.__comp7Controller.getRanksConfig()
        itemsArray = viewModel.getItems()
        itemsArray.clear()
        for rank in ranksConfig.ranksOrder:
            itemModel = ProgressionItemModel()
            itemModel.setHasRankInactivity(comp7_shared.hasRankInactivity(rank))
            meta_view_helper.setProgressionItemData(itemModel, viewModel, rank, ranksConfig)
            itemsArray.addViewModel(itemModel)

        itemsArray.invalidate()
