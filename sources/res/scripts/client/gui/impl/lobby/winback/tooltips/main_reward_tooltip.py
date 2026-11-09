# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/winback/tooltips/main_reward_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/winback/tooltips/main_reward_tooltip.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.winback.tooltips.main_reward_tooltip_model import MainRewardTooltipModel
from gui.impl.lobby.winback.winback_bonus_packer import getWinbackBonusPacker
from gui.impl.pub import ViewImpl
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData
if typing.TYPE_CHECKING:
    from typing import List
    from frameworks.wulf import Array
    from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
    from gui.server_events.bonuses import SimpleBonus

class MainRewardTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.winback.tooltips.main_reward_tooltip(), model=MainRewardTooltipModel())
        settings.args = args
        settings.kwargs = kwargs
        super(MainRewardTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MainRewardTooltip, self).getViewModel()

    def _onLoading(self, rewards):
        super(MainRewardTooltip, self)._onLoading()
        with self.viewModel.getRewards().transaction() as tx:
            self.__updateRewards(tx, rewards)

    def __updateRewards(self, model, rewards):
        model.clear()
        packMissionsBonusModelAndTooltipData(rewards, getWinbackBonusPacker(), model)
