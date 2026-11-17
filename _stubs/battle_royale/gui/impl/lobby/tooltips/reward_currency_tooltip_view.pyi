# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/reward_currency_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.reward_currency_tooltip_view_model import RewardCurrencyTooltipViewModel as RewardCurrencyTooltipViewModel
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.battle_royale_formatters import BRSections as BRSections
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType as CoinType
_PREMIUM_BONUS_CURRENCIES: tuple
_DAILY_BONUS_CURRENCIES: tuple

class RewardCurrencyTooltipView(ViewImpl):
    __battleResults: Any
    __currencyType: Any
    __arenaUniqueID: Any
    def __init__(self, currencyType, arenaUniqueID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
