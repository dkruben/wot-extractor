# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/vehicle_collector_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from backports.functools_lru_cache import lru_cache as lru_cache
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import MODULES_ANIMATION_SHOWN as MODULES_ANIMATION_SHOWN
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from nations import ALL_NATIONS_INDEX as ALL_NATIONS_INDEX
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items import ItemsCollection as ItemsCollection
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

# decorador original: @replace_none_kwargs(...)
def isAvailableForPurchase(vehicle, itemsCache=None):
    ...
def wasModulesAnimationShown():
    ...
# decorador original: @replace_none_kwargs(...)
def getCollectibleVehicles(nationID=..., itemsCache=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getCollectibleVehiclesInInventory(nationID=..., itemsCache=None):
    ...
# decorador original: @lru_cache(...)
def hasCollectibleVehicles(nationID=...):
    ...
def isAllCollectionPurchased(nationID):
    ...
