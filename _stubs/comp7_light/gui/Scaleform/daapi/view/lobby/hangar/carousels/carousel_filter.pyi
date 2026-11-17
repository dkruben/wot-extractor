# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/hangar/carousels/carousel_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import COMP7_LIGHT_CAROUSEL_FILTER_1 as COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2 as COMP7_LIGHT_CAROUSEL_FILTER_2, COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1 as COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1 as BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1 as BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, COMP7_LIGHT_CAROUSEL_FILTER_3 as COMP7_LIGHT_CAROUSEL_FILTER_3
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter as BattlePassCarouselFilter, BattlePassCriteriesGroup as BattlePassCriteriesGroup
from gui.filters.carousel_filter import EventCriteriesGroup as EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightCarouselFilter(BattlePassCarouselFilter):
    _serverSections: Any
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self):
        ...

class Comp7LightCriteriesGroup(BattlePassCriteriesGroup):
    __comp7LightController: Any
    _criteria: Any
    def update(self, filters):
        ...
    @classmethod
    def _comp7LightCriteria(cls, vehicle):
        ...
