# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/ranked_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem, formatSeasonLeftTime as formatSeasonLeftTime
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_ranked_model import ModeSelectorRankedModel as ModeSelectorRankedModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_ranked_widget_model import ModeSelectorRankedWidgetModel as ModeSelectorRankedWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_rank_model import ModeSelectorRankModel as ModeSelectorRankModel
from gui.ranked_battles.ranked_models import Rank as Rank
CALENDAR_ICON = ' %(calendarIcon)'

class RankedModeSelectorItem(ModeSelectorLegacyItem):
    __slots__: tuple
    _VIEW_MODEL = ModeSelectorRankedModel
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.RANKED
    __rankedBattleController: Any
    @property
    def viewModel(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def _getDisabledTooltipText(self):
        ...
    def __onGameModeUpdated(self, *_):
        ...
    def __getRankedName(self):
        ...
    def __getRankedNotActiveStatus(self):
        ...
    def __getTimeLeft(self):
        ...
    def __fillRankedWidget(self, model):
        ...
    @staticmethod
    def __fillRankData(model, rank):
        ...
    @staticmethod
    def __getRankedBattlesSeasonName(season):
        ...
