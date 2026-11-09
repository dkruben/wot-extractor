# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/sub_presenters/fort_rush_personal_rewards.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/sub_presenters/fort_rush_personal_rewards.py
from __future__ import absolute_import
import typing
from frameworks.wulf import Array
from fort_rush.gui.fort_rush_presenters_packers import FortRushPersonalRewards
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.fort_rush_reward_item_model import FortRushRewardItemModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import BattleResults

class FortRushPersonalRewardSubPresenter(BattleResultsSubPresenter):

    @classmethod
    def getViewModelType(cls):
        return Array[FortRushRewardItemModel]

    def packBattleResults(self, battleResults):
        with self.getViewModel().transaction() as model:
            FortRushPersonalRewards.packModel(model, battleResults)
