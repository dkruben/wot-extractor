# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/daily_quests_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.daily_tooltip_view_model import DailyTooltipViewModel as DailyTooltipViewModel
from halloween.gui.impl.lobby.hw_helpers import fillRewardsForTooltips as fillRewardsForTooltips
from typing import Optional as Optional
from gui.server_events.awards_formatters import PreformattedBonus as PreformattedBonus
from halloween.gui.impl.lobby.gsw_cards.quests_card_presenter import QuestData as QuestData

class DailyQuestsTooltip(ViewImpl):
    __slots__: tuple
    _MAX_BONUSES_IN_VIEW = 5
    __questData: Any
    def __init__(self, questData):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _isBonusEpicMedal(self, bonus):
        ...
