# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/vehicle_points_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.battle_pass.battle_pass_helpers import getSupportedCurrentArenaBonusType as getSupportedCurrentArenaBonusType
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel as RewardPointsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.vehicle_points_tooltip_view_model import VehiclePointsTooltipViewModel as VehiclePointsTooltipViewModel
from gui.impl.lobby.battle_pass.battle_pass_wot_plus import getWotPlusPerBattlePoints as getWotPlusPerBattlePoints, isValidWotPlusTier as isValidWotPlusTier, getWotPlusBattlePassTier as getWotPlusBattlePassTier
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.formatters.invites import getPreQueueName as getPreQueueName
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehiclePointsTooltipView(ViewImpl):
    __battlePassController: Any
    __itemsCache: Any
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, intCD, *args, **kwargs):
        ...
