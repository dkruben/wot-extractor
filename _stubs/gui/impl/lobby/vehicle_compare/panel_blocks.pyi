# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/panel_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.common.compare_toggle_ammunition_slot import CompareToggleAmmunitionSlot as CompareToggleAmmunitionSlot
from gui.impl.gen.view_models.views.lobby.tank_setup.common.compare_toggle_shell_ammunition_slot import CompareToggleShellAmmunitionSlot as CompareToggleShellAmmunitionSlot
from gui.impl.gen.view_models.views.lobby.tank_setup.common.specialization_model import SpecializationModel as SpecializationModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import OptDeviceBlock as OptDeviceBlock, BaseBlock as BaseBlock, ConsumablesBlock as ConsumablesBlock, BattleBoostersBlock as BattleBoostersBlock
from gui.impl.lobby.tank_setup.tank_setup_helper import createShellMechanicsModels as createShellMechanicsModels
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_MIN_MECHANIC_PRIORITY = 1

class CompareOptDeviceBlock(OptDeviceBlock):
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...
    def _updateSpecializations(self, slotModel, slotItem, idx):
        ...

class CompareShellsBlock(BaseBlock):
    __itemsCache: Any
    __selectedIndex: Any
    def __init__(self, vehicle, currentSection):
        ...
    def createBlock(self, viewModel):
        ...
    def updateBlock(self, viewModel):
        ...
    def _getSectionName(self):
        ...
    def _getAmmunitionSlotModel(self):
        ...
    def _getInstalled(self):
        ...
    def _getSetupLayout(self):
        ...
    def _getLayout(self):
        ...
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...

class CompareConsumablesBlock(ConsumablesBlock):
    def _getKeySettings(self):
        ...
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...

class CompareBattleBoostersBlock(BattleBoostersBlock):
    def _updateSlotWithItem(self, model, idx, slotItem):
        ...

class CompareCamouflageBlock(BaseBlock):
    def createBlock(self, viewModel):
        ...
    def updateBlock(self, viewModel):
        ...
    def _getSectionName(self):
        ...
    def _getAmmunitionSlotModel(self):
        ...
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...
    def _getSetupLayout(self):
        ...
    def _createSlots(self):
        ...
