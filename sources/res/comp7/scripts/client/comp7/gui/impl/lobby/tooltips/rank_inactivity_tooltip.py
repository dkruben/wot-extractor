# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/rank_inactivity_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/rank_inactivity_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.rank_inactivity_tooltip_model import RankInactivityTooltipModel
from gui.impl.pub import ViewImpl
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class RankInactivityTooltip(ViewImpl):
    __slots__ = ()
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.rank_inactivity_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = RankInactivityTooltipModel()
        super(RankInactivityTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RankInactivityTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(RankInactivityTooltip, self)._initialize(*args, **kwargs)
        playerDivision = comp7_shared.getPlayerDivision()
        rank = comp7_shared.getRankEnumValue(playerDivision)
        divisionByRank = comp7_shared.getPlayerDivisionByRankAndIndex(rank, playerDivision.index)
        self.viewModel.setRankInactivityCount(self.__comp7Controller.activityPoints)
        self.viewModel.setRankInactivityPointsCount(divisionByRank.ratingPointsPenalty)
