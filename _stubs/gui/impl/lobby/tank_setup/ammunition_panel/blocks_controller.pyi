# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/blocks_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import AmmunitionBlocksController as AmmunitionBlocksController
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.ammunition_panel.hangar_shells_counter_mapping import ShellCounterMapping as ShellCounterMapping
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class HangarAmmunitionBlocksController(AmmunitionBlocksController):
    __slots__: tuple
    settingsCore: Any
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateShells(self, viewModel, isFirst=False):
        ...
    def __isDisabled(self):
        ...
