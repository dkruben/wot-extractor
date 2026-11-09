# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/shell.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import CMLabel as CMLabel, option as option
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import TankSetupCMLabel as TankSetupCMLabel, FIRST_SLOT as FIRST_SLOT, SECOND_SLOT as SECOND_SLOT, THIRD_SLOT as THIRD_SLOT, BaseTankSetupContextMenu as BaseTankSetupContextMenu
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base_equipment import BaseHangarEquipmentSlotContextMenu as BaseHangarEquipmentSlotContextMenu
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from ids_generators import SequenceIDGenerator as SequenceIDGenerator

class ShellItemContextMenu(BaseTankSetupContextMenu):
    __sqGen: Any
    _slotsCount: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def putOnFirst(self):
        ...
    # decorador original: @option(...)
    def putOnSecond(self):
        ...
    # decorador original: @option(...)
    def putOnThird(self):
        ...
    def _sendPutOnSlotAction(self, onId):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _getVehicleItems(self):
        ...

class HangarShellItemContextMenu(BaseHangarEquipmentSlotContextMenu):
    _sqGen: Any
    _slotsCount: Any
    _shellsCounts: Any
    def _initFlashValues(self, ctx):
        ...
    def _applyShellCounts(self, layout):
        ...
    def _postProcessLayoutAfterSwap(self, layout):
        ...
    def _putOnAction(self, onId):
        ...
    def _isVisible(self, label):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _doPutOnAction(self, vehicle, callback):
        ...
    def _getVehicleItems(self):
        ...
