# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection as AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController, GroupData as GroupData
from gui.impl.common.ammunition_panel.base import BaseAmmunitionPanel as BaseAmmunitionPanel
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import BaseAmmunitionBlocksController as BaseAmmunitionBlocksController
from gui.impl.lobby.vehicle_compare.panel_blocks import CompareOptDeviceBlock as CompareOptDeviceBlock, CompareShellsBlock as CompareShellsBlock, CompareConsumablesBlock as CompareConsumablesBlock, CompareBattleBoostersBlock as CompareBattleBoostersBlock, CompareCamouflageBlock as CompareCamouflageBlock
_COMPARE_GROUPS: tuple

class CompareAmmunitionBlocksController(BaseAmmunitionBlocksController):
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
    def _updateCamouflage(self, viewModel, isFirst=False):
        ...
    def _createViewModel(self, name):
        ...

class CompareAmmunitionGroupsController(AmmunitionGroupsController):
    __slots__: tuple
    def _getGroups(self):
        ...
    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        ...

class CompareAmmunitionPanel(BaseAmmunitionPanel):
    __slots__: tuple
    def _createAmmunitionGroupsController(self, vehicle):
        ...
