# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/ammunition_panel/ammunition_blocks_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import OptDeviceBlock as OptDeviceBlock, ShellsBlock as ShellsBlock, ConsumablesBlock as ConsumablesBlock, BattleBoostersBlock as BattleBoostersBlock, BattleAbilitiesBlock as BattleAbilitiesBlock
from gui.impl.common.tabs_controller import TabsController as TabsController, tabUpdateFunc as tabUpdateFunc
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection as AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_shells_section import AmmunitionShellsSection as AmmunitionShellsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GroupData as GroupData

class BaseAmmunitionBlocksController(TabsController):
    __slots__: tuple
    _vehicle: Any
    _currentSection: Any
    _ctx: Any
    _sections: Any
    def __init__(self, vehicle, autoCreating=True, ctx=None):
        ...
    def updateVehicle(self, vehicle):
        ...
    def updateCurrentSection(self, currentSection):
        ...
    def getSectionsByGroup(self, groupID):
        ...
    def addSections(self, group):
        ...
    def getCurrentSection(self):
        ...
    def _getTabs(self, **kwargs):
        ...

class AmmunitionBlocksController(BaseAmmunitionBlocksController):
    __slots__: tuple
    # decorador original: @tabUpdateFunc(...)
    def _updateOptDevices(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateShells(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateConsumables(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateBattleBoosters(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateBattleAbilities(self, viewModel, isFirst=False):
        ...
    def _createViewModel(self, name):
        ...
