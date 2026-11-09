# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/util/vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleCompareEventHandler(C2WHandler):
    __comparisonBasket: Any
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @c2w(...)
    def __onComparisonBasketChange(self, *_):
        ...

class VehicleStateEventHandler(C2WHandler):
    __itemsCache: Any
    def init(self):
        ...
    def fini(self):
        ...
    def __onVehicleStateChanged(self, reason, diff):
        ...
    # decorador original: @c2w(...)
    def __sendVehicleState(self, vehicleCD):
        ...
