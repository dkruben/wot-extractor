# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/module_upd_available_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import namedtuple as namedtuple
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import isOutOfWallet as isOutOfWallet
from account_helpers import AccountSettings as AccountSettings
from constants import BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS
from helpers import dependency as dependency
from items import getTypeOfCompactDescr as getTypeOfCD
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

# base nao representavel no stub: namedtuple(...)
class _UnlockStats:
    def isUnlocked(self, vehIntCD):
        ...
    def isSeqUnlocked(self, seq):
        ...
    def getVehXP(self, vehIntCD):
        ...

# base nao representavel no stub: namedtuple(...)
class _VehicleResearchInfo:
    def __repr__(self):
        ...
    def hasUnviewedVehicles(self):
        ...
    def hasUnviewedItems(self):
        ...
    def getUnviewedItems(self):
        ...
    def getNewViewedItems(self):
        ...
    def hasNewViewed(self):
        ...
    def updateViewed(self):
        ...

def getResearchInfo(vehIntCD=None, vehicle=None):
    ...
def getVehicleResearchInfo(vehIntCD=None, vehicle=None):
    ...
def updateViewedItems(vehIntCD=None, vehicle=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isValidAccountType(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getVehicleResearchInfo(vehicle, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getNewCost(vehicleCD, level, oldCost, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getUnlockStats(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _validateAndGetVehicle(vehIntCD, vehicle, itemsCache=None):
    ...
def _marksAsViewedAndSave(vehicle, researchInfo):
    ...
def _validateVehicle(vehicle):
    ...
