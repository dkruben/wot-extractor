# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/customization/processors/cart.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.customization.shared import AdditionalPurchaseGroups as AdditionalPurchaseGroups, PurchaseItem as PurchaseItem, PURCHASE_ITEMS_ORDER as PURCHASE_ITEMS_ORDER, getAncestors as getAncestors
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from items.components.c11n_constants import SeasonType as SeasonType
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
_logger: Any
ProcessResult: Any

class ItemsType(CONST_CONTAINER):
    DEFAULT = 1
    STYLE = 2
    EDITABLE_STYLE = 3

class ProcessorSelector(object):
    __slots__: tuple
    __processors: Any
    def __init__(self, processors):
        ...
    def process(self, items):
        ...
    def __getItemsType(self, items):
        ...

class BasePurchaseDescription(object):
    __slots__: tuple
    _uiDataPacker: Any
    intCD: Any
    identificator: Any
    selected: Any
    item: Any
    component: Any
    quantity: Any
    purchaseIndices: Any
    progressionLevel: Any
    dependents: Any
    dependentOn: Any
    def __init__(self, item, purchaseIdx=0, quantity=1, component=None, progressionLevel=-1):
        ...
    def getUIData(self):
        ...
    def addPurchaseIndices(self, indices):
        ...
    def setPacker(self, packer):
        ...

class StubItemPurchaseDescription(BasePurchaseDescription):
    __slots__: tuple
    _StubItem: Any
    isFromInventory: Any
    isEdited: Any
    def __init__(self):
        ...

class SeparateItemPurchaseDescription(BasePurchaseDescription):
    __slots__: tuple
    selected: Any
    compoundPrice: Any
    isFromInventory: Any
    group: Any
    locked: Any
    isEdited: Any
    identificator: Any
    def __init__(self, purchaseItem, purchaseIdx, progressionLevel=-1):
        ...
    def _generateID(self):
        ...

class ItemsProcessor(object):
    __slots__: tuple
    _itemUiDataPacker: Any
    _stubUiDataPacker: Any
    _itemDescriptionClass: Any
    _stubItemDescriptionClass: Any
    def __init__(self, itemPacker, stubPacker):
        ...
    def process(self, items):
        ...
    def _preProcess(self, items):
        ...
    def _process(self, items):
        ...
    def _postProcess(self, itemsInfo):
        ...
    def _getStubItemDescription(self):
        ...
    def _getItemDescription(self, item, idx=0):
        ...

class SeparateItemsProcessor(ItemsProcessor):
    __slots__: tuple
    _itemDescriptionClass: Any
    def __init__(self, itemPacker, stubPacker):
        ...
    def _process(self, items):
        ...
    @staticmethod
    def _getKey(purchaseItem):
        ...

class StyleItemsProcessor(ItemsProcessor):
    __slots__: tuple
    __service: Any
    def _preProcess(self, items):
        ...
    def _process(self, style):
        ...
    def _getItemDescription(self, item, idx=0, progressionLevel=-1):
        ...

class EditableStyleItemsProcessor(SeparateItemsProcessor):
    __slots__: tuple
    __service: Any
    def _process(self, items):
        ...
    def _postProcess(self, itemsInfo):
        ...
    def _getItemDescription(self, item, idx=0, descriptionClass=None, descriptionPacker=None, progressionLevel=-1):
        ...
    def __updateStrictDependencies(self, descriptorsBySeasons):
        ...

class _SeasonPurchaseInfo(object):
    __slots__: tuple
    __buckets: Any
    __keyFunc: Any
    def __init__(self, keyFunc=None):
        ...
    def add(self, purchaseItemInfo, orderKey):
        ...
    def delete(self, intCD, orderKey):
        ...
    def flatten(self):
        ...
    @staticmethod
    def __defaultKeyFunc(item):
        ...
