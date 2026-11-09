# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/hw_ammunition_panel_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import cycle as cycle
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController, GroupData as GroupData
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import BaseAmmunitionBlocksController as BaseAmmunitionBlocksController
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import ConsumablesBlock as ConsumablesBlock, ShellsBlock as ShellsBlock
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection as AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_shells_section import AmmunitionShellsSection as AmmunitionShellsSection
from halloween.gui.impl.lobby.tank_setup import HWTankSetupConstants as HWTankSetupConstants
from halloween.gui.halloween_gui_constants import AmmoPanelSwitchPreset as AmmoPanelSwitchPreset
from halloween.gui.halloween_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys, setSettings as setSettings
AMMO_SECTIONS_DEFAULT: tuple
AMMO_SECTIONS_ALTERNATIVE: tuple
_PRESET_AMMO_SECTIONS: dict
_CMD_KEYS_123: tuple
_CMD_KEYS_456: tuple
_CMD_ACCELERATION_ABILITY_KEY = 'CMD_CM_VEHICLE_SWITCH_AUTOROTATION'
_PRESET_MAP_AMMO_KEYS: dict

class HWConsumablesBlock(ConsumablesBlock):
    def _getSectionName(self):
        ...
    def _getKeySettings(self):
        ...

class HWShellsBlock(ShellsBlock):
    def _getKeySettings(self):
        ...

class HWAmmunitionBlocksController(BaseAmmunitionBlocksController):
    # decorador original: @tabUpdateFunc(...)
    def _updateShells(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateHWConsumables(self, viewModel, isFirst=False):
        ...
    def _createViewModel(self, name):
        ...

class HWHangarAmmunitionGroupsController(AmmunitionGroupsController):
    __slots__: tuple
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
