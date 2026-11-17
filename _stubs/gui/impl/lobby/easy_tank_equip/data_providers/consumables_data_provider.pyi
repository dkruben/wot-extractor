# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/data_providers/consumables_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import OrderedDict as OrderedDict
from typing import TYPE_CHECKING as TYPE_CHECKING, NamedTuple as NamedTuple, List as List
from account_helpers.AccountSettings import EasyTankEquip as EasyTankEquip
from gui.easy_tank_equip.easy_tank_equip_helpers import getEasyTankEquipSetting as getEasyTankEquipSetting, setEasyTankEquipSetting as setEasyTankEquipSetting
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.consumables_preset_model import ConsumablesPresetType as ConsumablesPresetType
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo, SlotInfo as SlotInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.artefacts import Equipment as Equipment
from typing import Dict as Dict, Optional as Optional
_logger: Any
ConsumableTagsInfo: Any

class ConsumablesPresetSlotInfo(object):
    consumable: Any
    slotIdx: Any
    info: Any
    def __init__(self, consumable, info, slotIdx):
        ...

class ConsumablesPresetInfo(PresetInfo):
    presetType: Any
    items: Any
    def __init__(self, installed, storedItemsCount, installedItemsCount, itemPrice, presetType, items):
        ...

class ConsumablesDataProvider(BaseDataProvider):
    DEFAULT_CONFIG: dict
    REPLACE_CONSUMABLES_MAP: list
    PRESETS_ORDER: list
    __itemsCache: Any
    __consumablesOrder: Any
    __installedConsumables: Any
    __consumablesPresets: Any
    currentPresetIndex: Any
    isProposalSelected: Any
    presets: Any
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
    def getCurrentPresetItemsIds(self):
        ...
    def saveAccountSettings(self):
        ...
    def _getPresetDataForApplying(self):
        ...
    def __getPresetsInfo(self):
        ...
    def __getConsumablesPresetInfo(self, presetType, consumables):
        ...
    def __getConsumablesPresetItems(self, consumables):
        ...
    def __getSlotInfo(self, consumable):
        ...
    def __isConsumablesPresetInstalled(self, consumables):
        ...
    def __getConsumablesPresetsConfig(self):
        ...
    def __setConsumablesPresets(self, presetConfig):
        ...
    def __addBuiltInConsumables(self):
        ...
    def __cutPresetItems(self, hasBuiltIn=False):
        ...
    def __replaceConsumables(self):
        ...
    def __removeDuplicatePresets(self):
        ...
    def __sortPresets(self):
        ...
    def __getConsumable(self, itemTags):
        ...
