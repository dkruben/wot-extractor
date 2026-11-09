# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicles_data_providers/ls_vehicle_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CAROUSEL_FILTER_1 as CAROUSEL_FILTER_1, CAROUSEL_FILTER_2 as CAROUSEL_FILTER_2, CAROUSEL_FILTER_CLIENT_1 as CAROUSEL_FILTER_CLIENT_1
from gui.filters.carousel_filter import CarouselFilter as CarouselFilter
from helpers import dependency as dependency
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.skeletons.ls_controller import ILSController as ILSController

class LSBattleCarouselFilter(CarouselFilter):
    __lsController: Any
    _serverSections: Any
    _clientSections: Any
    _filters: Any
    def __init__(self):
        ...
    def save(self):
        ...
    def load(self):
        ...
