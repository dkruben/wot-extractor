# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/select_vehicle/filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import SELECT_VEHICLES_CAROUSEL_FILTER_1 as SELECT_VEHICLES_CAROUSEL_FILTER_1
from gui.filters.carousel_filter import BasicCriteriesGroup as BasicCriteriesGroup, CriteriesGroup as CriteriesGroup, SessionCarouselFilter as SessionCarouselFilter

class SelectVehiclesCriteriaGroup(BasicCriteriesGroup):
    def update(self, filters):
        ...

class SelectVehiclesCarouselFilter(SessionCarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self):
        ...
