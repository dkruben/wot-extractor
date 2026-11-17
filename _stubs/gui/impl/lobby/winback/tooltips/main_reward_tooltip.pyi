# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/tooltips/main_reward_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.tooltips.main_reward_tooltip_model import MainRewardTooltipModel as MainRewardTooltipModel
from gui.impl.lobby.winback.winback_bonus_packer import getWinbackBonusPacker as getWinbackBonusPacker
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from typing import List as List
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class MainRewardTooltip(ViewImpl):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, rewards):
        ...
    def __updateRewards(self, model, rewards):
        ...
