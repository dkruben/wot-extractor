# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/supply_slots_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING, Any as Any, Tuple as Tuple, Optional as Optional, Dict as Dict, Set as Set, Type as Type
from extension_utils import ResMgr as ResMgr, importClass as importClass
from ResMgr import DataSection as DataSection
from WeakMixin import WeakMixin as WeakMixin
from items import ITEM_TYPES as ITEM_TYPES, parseIntCompactDescr as parseIntCompactDescr, makeIntCompactDescrByID as makeIntCompactDescrByID, EQUIPMENT_TYPES as EQUIPMENT_TYPES, vehicles as vehicles
from items.basic_item import BasicItem as BasicItem
from items.components.supply_slot_categories import CategoriesHolder as CategoriesHolder, SlotCategories as SlotCategories
from items.vehicles import getItemByCompactDescr as getItemByCompactDescr
from nations import NONE_INDEX as NONE_INDEX
from soft_exception import SoftException as SoftException
from items.artefacts import Equipment as Equipment
_ITEM_TYPE_TO_SLOT_TYPE: dict

class SupplySlot(CategoriesHolder):
    __slots__: tuple
    itemType = None
    slotID: _Any
    categories: _Any
    tags: _Any
    def __init__(self):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    def readFromSection(self, section):
        ...
    def checkSlotCompatibility(self, compDescr=None, descr=None):
        ...
    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        ...
    def getSubType(self):
        ...
    @staticmethod
    def initSlot(slotSection):
        ...
    @staticmethod
    def makeCompactDescr(itemTypeID, idxWithinItemType):
        ...
    @staticmethod
    def parseCompactDescr(compDescr):
        ...
    def _readMeta(self, metaSection):
        ...

class OptionalDeviceSlot(SupplySlot):
    itemType = ITEM_TYPES.optionalDevice

class EquipmentSlot(SupplySlot):
    __slots__: tuple
    itemType = ITEM_TYPES.equipment
    equipmentType: _Any
    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        ...
    def _readMeta(self, metaSection):
        ...
    def getSubType(self):
        ...

class EpicEquipmentSlot(WeakMixin):
    FL_AVATAR_TAGS: _Any
    JOINING_TAGS: _Any
    @classmethod
    def fromEquipmentSlot(cls, equipmentSlot):
        ...
    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        ...

class ShellSlot(SupplySlot):
    itemType = ITEM_TYPES.shell

class SupplySlotsCache(object):
    __slots__: tuple
    __slotDescrs: _Any
    __categories: _Any
    def __init__(self, xmlPath=None):
        ...
    def readCacheFromFile(self, xmlPath):
        ...
    @property
    def slotDescrs(self):
        ...
    def getSlotDescr(self, slotID):
        ...
    def getSlotDescrsByTags(self, itags=..., etags=...):
        ...
    @property
    def categories(self):
        ...

def getSlotByItemTypeName(itemType):
    ...
