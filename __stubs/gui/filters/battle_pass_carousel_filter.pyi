# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/filters/battle_pass_carousel_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import CAROUSEL_FILTER_1 as CAROUSEL_FILTER_1, CAROUSEL_FILTER_2 as CAROUSEL_FILTER_2, CAROUSEL_FILTER_3 as CAROUSEL_FILTER_3, CAROUSEL_FILTER_CLIENT_1 as CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1 as BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1 as BATTLEPASS_CAROUSEL_FILTER_CLIENT_1
from gui.filters.carousel_filter import CarouselFilter as CarouselFilter, CustomizationCriteriesGroup as CustomizationCriteriesGroup, EventCriteriesGroup as EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass import BattlePassFilterConsts as BattlePassFilterConsts

class BattlePassCarouselFilter(CarouselFilter):
    __battlePassController: Any
    _serverSections: Any
    _clientSections: Any
    _criteriesGroups: Any
    currentSeasonID: Any
    def __init__(self):
        ...
    def save(self):
        ...
    def load(self):
        ...

class BattlePassCriteriesGroup(CustomizationCriteriesGroup):
    __battlePassController: Any
    _criteria: Any
    def update(self, filters):
        ...
    @classmethod
    def __isCommonProgression(cls, vehicle):
        ...
    def __addGeneralBattlePassCriteria(self):
        ...
