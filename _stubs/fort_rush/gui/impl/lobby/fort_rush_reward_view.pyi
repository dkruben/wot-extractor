# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from fort_rush.gui.impl.gen.view_models.views.lobby.fort_rush_rewards_screen_view_model import FortRushRewardsScreenViewModel as FortRushRewardsScreenViewModel
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from helpers import dependency as dependency
from frameworks.wulf import ViewFlags as ViewFlags
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from typing import Any as Any
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from frameworks.wulf import Array as Array
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker

class FortRushRewardView(ViewImpl):
    __ctrl: _Any
    __tooltips: _Any
    __rewardData: _Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onCloseClick(self):
        ...
    def __packRewards(self, rewardsModel, rewards, packer):
        ...
