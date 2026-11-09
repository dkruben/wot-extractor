# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/data_providers/opt_devices_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import OrderedDict as OrderedDict
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.game_control.wotlda.loadout_model import BaseOptDeviceLoadoutModel as BaseOptDeviceLoadoutModel
from gui.goodies.demount_kit import isDemountKitApplicableTo as isDemountKitApplicableTo, getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetDisableReason as PresetDisableReason
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalDisableReason as ProposalDisableReason
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.opt_devices_preset_model import OptDevicesPresetType as OptDevicesPresetType
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo, SlotInfo as SlotInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IWotPlusController as IWotPlusController, IEasyTankEquipController as IEasyTankEquipController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List, Optional as Optional, Dict as Dict
from gui.goodies.goodie_items import DemountKit as DemountKit
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.gui_items.vehicle_equipment import OptDeviceSlotData as OptDeviceSlotData
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.money import Money as Money
_logger: Any

class OptionalDevicesPresetInfo(PresetInfo):
    presetType: Any
    items: Any
    demountKits: Any
    disableReason: Any
    def __init__(self, itemPrice, presetType, items, demountKits=0, installed=False, storedItemsCount=0, installedItemsCount=0, disableReason=...):
        ...

class OptDevicesPresetSlotInfo(object):
    optDevice: Any
    slotIdx: Any
    slotData: Any
    info: Any
    def __init__(self, optDevice, slotData, info, slotIdx):
        ...

class OptDevicesPriorities(Enum):
    MODERNIZED_LEVEL_3 = 0
    DELUXE_LEVEL_2 = 1
    DELUXE_LEVEL_1 = 2
    TROPHY_UPGRADED = 3
    MODERNIZED_LEVEL_2 = 4
    MODERNIZED_LEVEL_1 = 5
    REGULAR = 6
    TROPHY_NOT_UPGRADED = 7

class OptDevicesDemountInfo(object):
    __itemsCache: Any
    __wotPlusController: Any
    forDemount: Any
    byMoney: Any
    byDemountKit: Any
    forFree: Any
    def __init__(self, forDemount):
        ...
    def initialize(self):
        ...
    def getDemountPrice(self):
        ...

class OptDevicesDataProvider(BaseDataProvider):
    __itemsCache: Any
    __easyTankEquipController: Any
    __installedOptDevices: Any
    __optDevicesCapacity: Any
    __optDevicesPresets: Any
    __optDevicesForDemount: Any
    currentPresetIndex: Any
    isProposalSelected: Any
    presets: Any
    proposalDisableReason: Any
    def __init__(self, vehicle, balance):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def setValuesFromCurrentPreset(self):
        ...
    def revertChangesFromSelectedPreset(self):
        ...
    def getPresets(self):
        ...
    def updatePresets(self, fullUpdate=False):
        ...
    def swapSlots(self, firstSlot, secondSlot):
        ...
    def isCurrentPresetDisableReasonChanged(self):
        ...
    def getCurrentPresetItemsIds(self):
        ...
    def _getPresetDataForApplying(self):
        ...
    def __getPresetsInfo(self):
        ...
    def __isAdvancedPresetNeeded(self, optDevices):
        ...
    def __isStandardPresetNeeded(self, optDevices):
        ...
    def __setOptDevicesPresets(self):
        ...
    def __getOptDevicesPresetInfo(self, presetType, optDevices):
        ...
    def __getOptDevicesPresetItems(self, optDevices):
        ...
    def __getSlotInfo(self, optDevice):
        ...
    def __isOptDevicesPresetInstalled(self, optDevices):
        ...
    def __getOptDevices(self, criteria):
        ...
    def __getAdvancedOptDevices(self, optDevicesTags, standardOptDevices):
        ...
    def __getStandardOptDevices(self, optDevicesTags):
        ...
    def __getOptDevicesForDemount(self, optDevices):
        ...
    def __getInstalledPresetInfo(self, presetType):
        ...
    @staticmethod
    def __getDemountNotPossiblePresetInfo(presetType, presetItems, demountItemsPrice, demountKits):
        ...
    @staticmethod
    def __getOptDeviceIndex(optDevice):
        ...
    def __installOptDevices(self, devices):
        ...
