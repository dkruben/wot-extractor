# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/data_providers/shells_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from copy import copy as copy
from typing import TYPE_CHECKING as TYPE_CHECKING
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers.AccountSettings import EasyTankEquip as EasyTankEquip
from gui.easy_tank_equip.easy_tank_equip_helpers import getEasyTankEquipSetting as getEasyTankEquipSetting, setEasyTankEquipSetting as setEasyTankEquipSetting
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.shells_preset_model import ShellsPresetType as ShellsPresetType
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider, PresetInfo as PresetInfo, SlotInfo as SlotInfo
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.items_parameters import getShellsLoadSize as getShellsLoadSize
from helpers import dependency as dependency
from skeletons.gui.game_control import IEasyTankEquipController as IEasyTankEquipController
from typing import List as List, Optional as Optional, Dict as Dict
from gui.shared.gui_items.vehicle_modules import Shell as Shell

class ShellsPresetSlotInfo(object):
    shell: Any
    slotIdx: Any
    info: Any
    mechanics: Any
    def __init__(self, shell, info, slotIdx, mechanics):
        ...

class ShellsPresetInfo(PresetInfo):
    presetType: Any
    items: Any
    def __init__(self, installed, storedItemsCount, installedItemsCount, itemPrice, presetType, items):
        ...

class ShellsDataProvider(BaseDataProvider):
    __easyTankEquipCtrl: Any
    __installedShells: Any
    __shellsPresets: Any
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
    def __getShellsPresetInfo(self, presetType, shells):
        ...
    def __getShellsPresetItems(self, shells):
        ...
    def __getSlotInfo(self, shell):
        ...
    def __isShellsPresetInstalled(self, shells):
        ...
    def __getAdvancedShells(self, shells, clipSize):
        ...
    def __getMechanics(self, shell):
        ...
    @staticmethod
    def __sortPresetByAnother(shells, sampleShells):
        ...
    def __setShellsPresets(self):
        ...
