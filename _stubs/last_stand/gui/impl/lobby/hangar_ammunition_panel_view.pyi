# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/hangar_ammunition_panel_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import cycle as cycle
from helpers import dependency as dependency
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController, GroupData as GroupData
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import BaseAmmunitionBlocksController as BaseAmmunitionBlocksController
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import ConsumablesBlock as ConsumablesBlock, ShellsBlock as ShellsBlock, OptDeviceBlock as OptDeviceBlock, BattleBoostersBlock as BattleBoostersBlock
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection as AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_shells_section import AmmunitionShellsSection as AmmunitionShellsSection
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants as LSTankSetupConstants
from last_stand.gui.ls_gui_constants import AmmoPanelSwitchPreset as AmmoPanelSwitchPreset
from last_stand.gui.ls_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys, setSettings as setSettings
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from LSAccountEquipmentController import getLSConsumables as getLSConsumables
LS_GROUPS: tuple
LS_GROUPS_ALTERNATIVE: tuple
_PRESET_AMMO_SECTIONS: dict
_CMD_KEYS_123: tuple
_CMD_KEYS_456: tuple
_PRESET_MAP_AMMO_KEYS: dict

class LSConsumablesBlock(ConsumablesBlock):
    def _getSectionName(self):
        ...
    def _getKeySettings(self):
        ...
    def _getInstalled(self):
        ...
    def _getLayout(self):
        ...

class LSShellsBlock(ShellsBlock):
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...
    def _getKeySettings(self):
        ...

class LSAmmunitionBlocksController(BaseAmmunitionBlocksController):
    # decorador original: @tabUpdateFunc(...)
    def _updateShells(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateLSConsumables(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateOptDevices(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateBattleBoosters(self, viewModel, isFirst=False):
        ...
    def _createViewModel(self, name):
        ...

class LSHangarAmmunitionGroupsController(AmmunitionGroupsController):
    _guiLoader: Any
    _presetCycle: Any
    def __init__(self, vehicle, autoCreating=True, ctx=None):
        ...
    def finalize(self):
        ...
    def setNextPreset(self, viewModel=None):
        ...
    def _getGroups(self):
        ...
    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        ...
    @staticmethod
    def _setPreset(presetNum):
        ...
    @staticmethod
    def _getPreset():
        ...
