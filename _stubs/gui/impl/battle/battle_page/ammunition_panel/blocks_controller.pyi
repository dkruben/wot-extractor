# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/blocks_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import AmmunitionBlocksController as AmmunitionBlocksController
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_shell_ammunition_slot import PrebattleShellAmmunitionSlot as PrebattleShellAmmunitionSlot, ShellBattleState as ShellBattleState
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import ShellsBlock as ShellsBlock, ConsumablesBlock as ConsumablesBlock
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from gui.shared.gui_items import Vehicle as Vehicle
_EMPTY_INT_COMPACT_DESCRIPTOR = 0

class PrebattleShellsBlock(ShellsBlock):
    __nextShellIntCD: Any
    __currentShellIntCD: Any
    def __init__(self, vehicle, currentSection, nextShellIntCD, currentShellIntCD):
        ...
    def _getAmmunitionSlotModel(self):
        ...
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...
    def __getShellState(self, slotItem):
        ...

class RespawnConsumablesBlock(ConsumablesBlock):
    def _getKeySettings(self):
        ...

class RespawnShellsBlock(ShellsBlock):
    def _getKeySettings(self):
        ...

class PrebattleAmmunitionBlocksController(AmmunitionBlocksController):
    __settingsCore: Any
    __slots__: tuple
    __nextShellIntCD: Any
    __currentShellIntCD: Any
    def __init__(self, vehicle, autoCreating=True, ctx=None):
        ...
    def onNextShellChanged(self, intCD):
        ...
    def onCurrentShellChanged(self, intCD):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateShells(self, viewModel, isFirst=False):
        ...

class RespawnAmmunitionBlocksController(AmmunitionBlocksController):
    # decorador original: @tabUpdateFunc(...)
    def _updateShells(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateConsumables(self, viewModel, isFirst=False):
        ...
