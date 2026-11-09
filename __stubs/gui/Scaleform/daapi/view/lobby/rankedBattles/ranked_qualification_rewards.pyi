# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_qualification_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from helpers import dependency as dependency
from shared_utils import first as first
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.ranked.ranked_qualification_rewards_view_model import RankedQualificationRewardsViewModel as RankedQualificationRewardsViewModel
from gui.impl.gen.view_models.views.lobby.ranked.ranked_qualification_rewards_battle_bonus_model import RankedQualificationRewardsBattleBonusModel as RankedQualificationRewardsBattleBonusModel
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.ranked_battles.constants import ZERO_RANK_ID as ZERO_RANK_ID
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedQualificationRewardsView(ViewImpl):
    __slots__: tuple
    __rankedController: Any
    __tooltipItems: Any
    __quests: Any
    __totalBattles: Any
    __currentBattles: Any
    def __init__(self, flags=...):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def __update(self):
        ...
    def __updateData(self):
        ...
    def __updateViewModel(self):
        ...

class RankedQualificationRewards(InjectComponentAdaptor):
    __view: Any
    def _makeInjectView(self):
        ...
