# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/battle_ability.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import option as option, CMLabel as CMLabel
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import TankSetupCMLabel as TankSetupCMLabel
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base_equipment import BaseEquipmentItemContextMenu as BaseEquipmentItemContextMenu, BaseEquipmentSlotContextMenu as BaseEquipmentSlotContextMenu, BaseHangarEquipmentSlotContextMenu as BaseHangarEquipmentSlotContextMenu
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from ids_generators import SequenceIDGenerator as SequenceIDGenerator

class BattleAbilityItemContextMenu(BaseEquipmentItemContextMenu):
    _sqGen: Any
    _slotsCount: Any
    def _initFlashValues(self, ctx):
        ...
    def _isVisible(self, label):
        ...
    def _getVehicleItems(self):
        ...

class BattleAbilitySlotContextMenu(BaseEquipmentSlotContextMenu):
    _sqGen: Any
    _slotsCount: Any
    # decorador original: @option(...)
    def takeOff(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _isVisible(self, label):
        ...
    def _getVehicleItems(self):
        ...

class HangarBattleAbilitySlotContextMenu(BaseHangarEquipmentSlotContextMenu):
    _sqGen: Any
    _slotsCount: Any
    # decorador original: @option(...)
    # decorador original: @adisp_process
    def takeOff(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _putOnAction(self, onId):
        ...
    def _getCopyVehicle(self):
        ...
    def _isVisible(self, label):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        ...
    def _getVehicleItems(self):
        ...
