# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/rank_compatibility_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/rank_compatibility_tooltip.py
from __future__ import absolute_import
from typing import Optional
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.rank_compatibility_tooltip_model import RankCompatibilityTooltipModel
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class RankCompatibilityTooltip(ViewImpl):
    __slots__ = ('__rankRangeRestriction', '__squadSize')
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, squadSize, rankRngRestr, layoutID=R.views.comp7.mono.lobby.tooltips.rank_compatibility_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = RankCompatibilityTooltipModel()
        self.__squadSize = squadSize
        self.__rankRangeRestriction = rankRngRestr
        super(RankCompatibilityTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RankCompatibilityTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(RankCompatibilityTooltip, self)
        with self.viewModel.transaction() as tx:
            tx.setSeasonName(getSeasonNameEnum(self.__comp7Controller, SeasonName))
            tx.setRankRangeRestriction(self.__rankRangeRestriction)
            tx.setSquadSize(self.__squadSize)
