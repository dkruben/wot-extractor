# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/battle_booster.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui import shop as shop
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import CMLabel as CMLabel, option as option
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import BaseItemContextMenu as BaseItemContextMenu, BaseSlotContextMenu as BaseSlotContextMenu, TankSetupCMLabel as TankSetupCMLabel
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base_equipment import BaseHangarEquipmentSlotContextMenu as BaseHangarEquipmentSlotContextMenu
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents as TankSetupSoundEvents
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from ids_generators import SequenceIDGenerator as SequenceIDGenerator

class BattleBoosterItemContextMenu(BaseItemContextMenu):
    __sqGen: Any
    # decorador original: @option(...)
    def select(self):
        ...
    # decorador original: @option(...)
    def buyMore(self):
        ...
    def _isVisible(self, label):
        ...
    def _getVehicleItems(self):
        ...

class BattleBoosterSlotContextMenu(BaseSlotContextMenu):
    __sqGen: Any
    # decorador original: @option(...)
    def buyMore(self):
        ...
    # decorador original: @option(...)
    def unload(self):
        ...
    # decorador original: @option(...)
    def takeOff(self):
        ...
    def _isVisible(self, label):
        ...
    def _getVehicleItems(self):
        ...

class HangarBattleBoosterSlotContextMenu(BaseHangarEquipmentSlotContextMenu):
    _sqGen: Any
    # decorador original: @option(...)
    def buyMore(self):
        ...
    # decorador original: @option(...)
    def unload(self):
        ...
    # decorador original: @option(...)
    def takeOffFromSlot(self):
        ...
    def _isVisible(self, label):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        ...
    def _getVehicleItems(self):
        ...
    # decorador original: @adisp_process
    def __unloadAction(self):
        ...
