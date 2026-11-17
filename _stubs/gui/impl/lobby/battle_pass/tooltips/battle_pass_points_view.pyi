# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_points_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_points_view_model import BattlePassPointsViewModel as BattlePassPointsViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel as RewardPointsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.vehicle_item_model import VehicleItemModel as VehicleItemModel
from gui.impl.lobby.battle_pass.battle_pass_wot_plus import getWotPlusPerBattlePoints as getWotPlusPerBattlePoints, getWotPlusBattlePassTier as getWotPlusBattlePassTier, isValidWotPlusTier as isValidWotPlusTier
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class BattlePassPointsTooltip(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __battlePassController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __setPointsInfo(self, model):
        ...
