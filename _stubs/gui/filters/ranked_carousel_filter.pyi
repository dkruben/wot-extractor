# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/filters/ranked_carousel_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers.AccountSettings import RANKED_CAROUSEL_FILTER_1 as RANKED_CAROUSEL_FILTER_1, RANKED_CAROUSEL_FILTER_2 as RANKED_CAROUSEL_FILTER_2, RANKED_CAROUSEL_FILTER_CLIENT_1 as RANKED_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1 as BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1 as BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, RANKED_CAROUSEL_FILTER_3 as RANKED_CAROUSEL_FILTER_3
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter as BattlePassCarouselFilter, BattlePassCriteriesGroup as BattlePassCriteriesGroup
from gui.filters.carousel_filter import EventCriteriesGroup as EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
_logger: Any

class RankedCarouselFilter(BattlePassCarouselFilter):
    _serverSections: Any
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self):
        ...

class RankedCriteriesGroup(BattlePassCriteriesGroup):
    __rankedBattlesController: Any
    _criteria: Any
    def update(self, filters):
        ...
    @classmethod
    def _rankedCriteria(cls, vehicle):
        ...
