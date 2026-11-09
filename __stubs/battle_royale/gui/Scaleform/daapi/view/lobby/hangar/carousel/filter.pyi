# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import ROYALE_CAROUSEL_FILTER_1 as ROYALE_CAROUSEL_FILTER_1, ROYALE_CAROUSEL_FILTER_2 as ROYALE_CAROUSEL_FILTER_2, ROYALE_CAROUSEL_FILTER_CLIENT_1 as ROYALE_CAROUSEL_FILTER_CLIENT_1
from gui.filters import carousel_filter as carousel_filter

class RoyaleCarouselFilter(carousel_filter.CarouselFilter):
    _serverSections: Any
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self):
        ...
    def _setCriteriaGroups(self):
        ...
    def _getFromServerStorage(self, defaultFilters):
        ...
