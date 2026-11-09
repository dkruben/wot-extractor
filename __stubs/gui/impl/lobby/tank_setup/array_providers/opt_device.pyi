# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/array_providers/opt_device.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from itertools import izip as izip, chain as chain
import typing as typing
from gui.impl import backport as backport
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.bonus_value_model import BonusValueModel as BonusValueModel
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specialization_model import SpecializationModel as SpecializationModel
from gui.impl.gen.view_models.views.lobby.tank_setup.deconstruct_item_model import DeconstructItemModel as DeconstructItemModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_slot_model import OptDeviceSlotModel as OptDeviceSlotModel
from gui.impl.lobby.tank_setup.array_providers.base import VehicleBaseArrayProvider as VehicleBaseArrayProvider, BaseArrayProvider as BaseArrayProvider
from gui.impl.lobby.tank_setup.tank_setup_helper import getCategoriesMask as getCategoriesMask
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import ZERO_MONEY as ZERO_MONEY
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from shared_utils import first as first
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
from gui.impl.lobby.tank_setup.array_providers.base import BaseVehSectionContext as BaseVehSectionContext
_logger: Any

class ListTypes(object):
    STORAGE = 'storage'
    ON_VEHICLE = 'onVehicle'

class ArrayOptDeviceProvider(BaseArrayProvider):
    def updateSlot(self, model, item, ctx):
        ...
    def _getItemTypeID(self):
        ...
    def _getItemSortKey(self, item, ctx):
        ...
    @staticmethod
    def _fillBonuses(model, item):
        ...
    @staticmethod
    def _fillEffects(model, item):
        ...
    def _fillVehicle(self, model, vehCD):
        ...

class DeconstructOptDeviceStorageProvider(ArrayOptDeviceProvider):
    def getLimit(self, item, upgradedPair):
        ...
    def getItemViewModel(self):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _fillSelectedCount(self, model, item, ctx):
        ...
    def _fillStorageCount(self, model, item, ctx):
        ...
    def _getCriteria(self):
        ...
    def getTotalPrice(self, ctx):
        ...
    def getFilterFunc(self, upgradedPair):
        ...

class DeconstructOptDeviceOnVehicleProvider(ArrayOptDeviceProvider):
    def getItemsList(self):
        ...
    def getItemViewModel(self):
        ...
    def updateSlot(self, model, itemPair, ctx):
        ...
    def _fillSelectedCount(self, model, itemPair, ctx):
        ...
    def getTotalPrice(self, ctx):
        ...
    def getFilterFunc(self, upgradedPair):
        ...
    def _getItemSortKey(self, item, ctx):
        ...

class BaseOptDeviceProvider(VehicleBaseArrayProvider):
    _wotPlusController: Any
    __slots__: tuple
    def getItemViewModel(self):
        ...
    def _fillWotPlusStatus(self, model, item):
        ...
    def createSlot(self, item, ctx):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _fillSpecializations(self, model, item, slotID):
        ...
    def _fillBonuses(self, model, item, slotID):
        ...
    @staticmethod
    def _fillEffects(model, item):
        ...
    @classmethod
    def _getItemTypeID(cls):
        ...
    def _getEquipment(self):
        ...
    def _getItemSortKey(self, item, ctx):
        ...
    def __getAppropriateCategories(self, item, slotID):
        ...

class SimpleOptDeviceProvider(BaseOptDeviceProvider):
    __slots__: tuple
    def _getItemCriteria(self):
        ...

class DeluxeOptDeviceProvider(BaseOptDeviceProvider):
    _lobbyCtx: Any
    __slots__: tuple
    def createSlot(self, item, ctx):
        ...
    def _getItemSortKey(self, item, ctx):
        ...
    @staticmethod
    def _fillHighlight(model, item):
        ...
    def _getItemCriteria(self):
        ...

class ModernisedOptDeviceProvider(DeluxeOptDeviceProvider):
    __slots__: tuple
    def createSlot(self, item, ctx):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    @staticmethod
    def _fillHighlight(model, item):
        ...
    def _getItemSortKey(self, item, ctx):
        ...
    def _sortItems(self, items, ctx):
        ...
    def _getItemCriteria(self):
        ...

class TrophyOptDeviceProvider(DeluxeOptDeviceProvider):
    def _getItemSortKey(self, item, ctx):
        ...
    def _sortItems(self, items, ctx):
        ...
    @staticmethod
    def _fillHighlight(model, item):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _getItemCriteria(self):
        ...
    def _isInstallAllowed(self, item):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _getInstalledSet(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getModernizedInstalledList(itemsCache=None):
    ...
