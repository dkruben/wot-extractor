# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/controllers/fun_random_ammo_groups_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random.gui.impl.gen.view_models.views.lobby.loadout.fun_random_loadout_constants import FunRandomLoadoutConstants as FunRandomLoadoutConstants
from fun_random.gui.impl.lobby.hangar.controllers.fun_random_ammo_blocks_controller import FunRandomHangarAmmunitionBlocksController as FunRandomHangarAmmunitionBlocksController
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GroupData as GroupData, SWITCHABLE_SECTIONS as SWITCHABLE_SECTIONS
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.ammunition_panel.groups_controller import HangarAmmunitionGroupsController as HangarAmmunitionGroupsController
from fun_random.gui.feature.configs.sub_modes.sub_mode import FunSubModeCompositeConfigurationModel as FunSubModeCompositeConfigurationModel

class FunRandomHangarAmmunitionGroupsController(HangarAmmunitionGroupsController, FunSubModesWatcher):
    __slots__: tuple
    def _isSwitchEnabled(self, groupSettings):
        ...
    def _getGroups(self):
        ...
    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __getSubModeGroups(self):
        ...
