# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSAccountEquipmentController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import logging as logging
import BigWorld as BigWorld
import weakref as weakref
import functools as functools
from last_stand_common import ls_account_commands as ls_account_commands, last_stand_constants as last_stand_constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from items import vehicles as vehicles
from PlayerEvents import g_playerEvents as g_playerEvents
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from gui.shared.gui_items.vehicle_equipment import _ExpendableEquipment as _ExpendableEquipment
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.utils.requesters import getDiffID as getDiffID
_logger: Any

class _ExtConsumables(object):
    __slots__: tuple
    layout: Any
    installed: Any
    isAutoEquip: Any
    def __init__(self, layout, installed, isAutoEquip):
        ...

class _ExtExpendableEquipment(_ExpendableEquipment):
    __slots__: tuple
    def _createItem(self, intCD):
        ...

class LSInventorySessionCache(object):
    DATA_KEY = last_stand_constants.LS_INVENTORY_PDATA_KEY
    extendedInventoryCache = None
    vehObjsCache = None
    @classmethod
    def inventory(cls):
        ...
    @classmethod
    def init(cls):
        ...
    @classmethod
    def getCachedEquipment(cls, obj, initializer):
        ...
    @classmethod
    def vehInventoryInvalidator(cls, params):
        ...
    @classmethod
    def _onClientSynchronize(cls, isFullSync, diff):
        ...
    @classmethod
    def __deleteInstance(cls):
        ...
    @classmethod
    def __delCachedEquipment(cls, objID, _):
        ...

class LSAccountEquipmentController(BigWorld.StaticScriptComponent):
    EMPTY_LAYOUT: list
    itemsCache: Any
    _vehObject: Any
    _vehInvID: Any
    def __init__(self):
        ...
    @property
    def inventory(self):
        ...
    def getVehicleLayout(self, vehInvID):
        ...
    def getVehicleInventory(self, vehInvID):
        ...
    def getVehicleSettings(self, vehInvID):
        ...
    def isVehicleAutoEquipEnabled(self, vehInvID):
        ...
    def getExtConsumables(self, vehicle):
        ...
    def updateSelectedEquipment(self, vehInvID, eqList, callback=None):
        ...
    def setAutoMaintenanceEnabled(self, vehInvID, isEnabled, callback=None):
        ...
    def _createExtendedConsumables(self, vehicle):
        ...
    def devSetLayout(self, layout, invID=None):
        ...
    def devSetAutoMaintenanceEnabled(self, isEnabled, invID=None):
        ...
    def __devGetEqCompDescr(self, equipment):
        ...

def getLSConsumables(vehicle):
    ...
def devSetLayout(layout, invID=None):
    ...
def devSetAutoMaintenanceEnabled(isEnabled, invID=None):
    ...
