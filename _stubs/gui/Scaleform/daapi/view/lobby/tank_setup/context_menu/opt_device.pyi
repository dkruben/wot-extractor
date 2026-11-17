# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/opt_device.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import option as option, CMLabel as CMLabel
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import TankSetupCMLabel as TankSetupCMLabel
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base_equipment import BaseEquipmentItemContextMenu as BaseEquipmentItemContextMenu, BaseEquipmentSlotContextMenu as BaseEquipmentSlotContextMenu, BaseHangarEquipmentSlotContextMenu as BaseHangarEquipmentSlotContextMenu
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents as TankSetupSoundEvents
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from gui.game_control.wot_plus_controller import WotPlusController as WotPlusController

class OptDeviceItemContextMenu(BaseEquipmentItemContextMenu):
    _sqGen: Any
    _slotsCount: Any
    def _initFlashValues(self, ctx):
        ...
    def _upgradeEquipment(self):
        ...
    def _getVehicleItems(self):
        ...

class OptDeviceSlotContextMenu(BaseEquipmentSlotContextMenu):
    _sqGen: Any
    _wotPlusController: Any
    _slotsCount: Any
    # decorador original: @option(...)
    def demount(self):
        ...
    # decorador original: @option(...)
    def demountFromSetup(self):
        ...
    # decorador original: @option(...)
    def demountFromSetups(self):
        ...
    # decorador original: @option(...)
    def destroy(self):
        ...
    # decorador original: @option(...)
    def deconstruct(self):
        ...
    # decorador original: @option(...)
    def takeOff(self):
        ...
    # decorador original: @option(...)
    def unload(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _isVisible(self, label):
        ...
    def _upgradeEquipment(self):
        ...
    def _getVehicleItems(self):
        ...

class HangarOptDeviceSlotContextMenu(BaseHangarEquipmentSlotContextMenu):
    _sqGen: Any
    _wotPlusController: Any
    _slotsCount: Any
    # decorador original: @option(...)
    def demount(self):
        ...
    # decorador original: @option(...)
    def demountFromSetup(self):
        ...
    # decorador original: @option(...)
    def demountFromSetups(self):
        ...
    # decorador original: @option(...)
    def destroy(self):
        ...
    # decorador original: @option(...)
    def deconstruct(self):
        ...
    # decorador original: @adisp_process
    def _deconstruct(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    # decorador original: @adisp_process
    def _demountProcess(self, isDestroy=False, everywhere=True):
        ...
    def _putOnAction(self, onId):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        ...
    def _upgradeEquipment(self):
        ...
    def _getVehicleItems(self):
        ...
    def _isVisible(self, label):
        ...
