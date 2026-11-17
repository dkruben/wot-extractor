# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/filters/fort_rush_carousel_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import FORT_RUSH_CAROUSEL_FILTER_1 as FORT_RUSH_CAROUSEL_FILTER_1
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.filters.carousel_filter import CustomizationCriteriesGroup as CustomizationCriteriesGroup, FILTER_KEYS as FILTER_KEYS, SessionCarouselFilter as SessionCarouselFilter
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency

class FortRushCriteriesGroup(CustomizationCriteriesGroup):
    __battleController: Any
    _criteria: Any
    def update(self, filters):
        ...
    @classmethod
    def __isSuitableVehicle(cls, vehicle):
        ...

class FortRushCarouselFilter(SessionCarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self):
        ...
    def _setCriteriaGroups(self):
        ...
