# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/controllers/fun_random_ammo_blocks_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.feature.fun_constants import FunCustomShellsSource as FunCustomShellsSource
from fun_random.gui.feature.models.custom_abilities import FunCustomAbilitySlot as FunCustomAbilitySlot
from fun_random.gui.feature.models.custom_shells import FunCustomShellSlot as FunCustomShellSlot
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random.gui.impl.gen.view_models.views.lobby.loadout.fun_random_loadout_constants import FunRandomLoadoutConstants as FunRandomLoadoutConstants
from fun_random.gui.impl.gen.view_models.views.lobby.loadout.shells.fun_random_custom_ability_slot import FunRandomCustomAbilitySlot as FunRandomCustomAbilitySlot
from fun_random.gui.impl.gen.view_models.views.lobby.loadout.shells.fun_random_custom_shell_slot import FunRandomCustomShellSlot as FunRandomCustomShellSlot
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import BaseBlock as BaseBlock
from gui.impl.lobby.tank_setup.ammunition_panel.blocks_controller import HangarAmmunitionBlocksController as HangarAmmunitionBlocksController

class FunRandomCustomBaseBlock(BaseBlock, FunSubModesWatcher):
    def createBlock(self, viewModel):
        ...
    def _getKeySettings(self):
        ...
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getSetupLayout(self):
        ...
    def _getSubModeCustomSlots(self):
        ...

class FunRandomCustomShellsBlock(FunRandomCustomBaseBlock):
    def _getAmmunitionSlotModel(self):
        ...
    def _getSectionName(self):
        ...
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _getSubModeCustomSlots(self):
        ...

class FunRandomCustomAbilitiesBlock(FunRandomCustomBaseBlock):
    def _getAmmunitionSlotModel(self):
        ...
    def _getSectionName(self):
        ...
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _getSubModeCustomSlots(self):
        ...

class FunRandomHangarAmmunitionBlocksController(HangarAmmunitionBlocksController):
    # decorador original: @tabUpdateFunc(...)
    def _updateFunRandomCustomShells(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateFunRandomCustomAbilities(self, viewModel, isFirst=False):
        ...
