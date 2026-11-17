# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/account_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import wg_async as wg_async
import constants as constants
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from items import vehicles as vehicles, tankmen as tankmen, ITEM_TYPE_NAMES as ITEM_TYPE_NAMES
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from soft_exception import SoftException as SoftException
_logger: Any

class ValidateException(SoftException):
    code: Any
    itemData: Any
    def __init__(self, msg, code, itemData):
        ...

class ValidationCodes(object):
    OK = 0
    VEHICLE_MISMATCH = 1001
    CHASSIS_MISMATCH = 1002
    TURRET_MISMATCH = 1003
    GUN_MISMATCH = 1004
    ENGINE_MISMATCH = 1005
    FUEL_TANK_MISMATCH = 1006
    RADIO_MISMATCH = 1007
    TANKMEN_MISMATCH = 1008
    OPT_DEV_MISMATCH = 1009
    SHELL_MISMATCH = 1010
    EQ_MISMATCH = 1011
    VEHICLE_CREW_MISMATCH = 1012
    OUTFIT_MISMATCH = 1013
    UNLOCKS_MISMATCH = 1014

class AccountValidator(object):
    itemsCache: Any
    itemsFactory: Any
    # decorador original: @wg_async.wg_async
    def validate(self, callback=None):
        ...
    def _getHandlers(self):
        ...

class InventoryVehiclesValidator(AccountValidator):
    def _getHandlers(self):
        ...
    # decorador original: @wg_async.wg_async
    def __validateInventoryVehicles(self):
        ...

class InventoryOutfitValidator(AccountValidator):
    def _getHandlers(self):
        ...
    # decorador original: @wg_async.wg_async
    def __validateInventoryOutfit(self):
        ...

class InventoryTankmenValidator(AccountValidator):
    def _getHandlers(self):
        ...
    # decorador original: @wg_async.wg_async
    def __validateInventoryTankmen(self):
        ...

def _packItemData(itemTypeID, itemData, *args):
    ...
