# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/base_equipment.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import CMLabel as CMLabel, option as option
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import BaseItemContextMenu as BaseItemContextMenu, BaseSlotContextMenu as BaseSlotContextMenu, TankSetupCMLabel as TankSetupCMLabel, FIRST_SLOT as FIRST_SLOT, SECOND_SLOT as SECOND_SLOT, THIRD_SLOT as THIRD_SLOT
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID
from gui.shared.event_dispatcher import showModuleInfo as showModuleInfo
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class BaseEquipmentItemContextMenu(BaseItemContextMenu):
    __lobbyContext: Any
    _sqGen: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def upgrade(self):
        ...
    # decorador original: @option(...)
    def select(self):
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
    def _getOptionCustomData(self, label):
        ...
    def _isVisible(self, label):
        ...
    def _upgradeEquipment(self):
        ...

class BaseEquipmentSlotContextMenu(BaseSlotContextMenu):
    __lobbyContext: Any
    _sqGen: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def upgrade(self):
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
    def _isVisible(self, label):
        ...
    def _upgradeEquipment(self):
        ...

class BaseHangarEquipmentSlotContextMenu(BaseSlotContextMenu):
    __lobbyContext: Any
    _sqGen: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def upgrade(self):
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
    def _getVehicle(self):
        ...
    def _showInfo(self):
        ...
    def _putOnAction(self, onId):
        ...
    def _postProcessLayoutAfterSwap(self, layout):
        ...
    # decorador original: @adisp_process
    def _makePutOnAction(self, setupName, onId, copyVehicle, layout):
        ...
    # decorador original: @adisp_async
    def _doPutOnAction(self, vehicle, callback):
        ...
    def _isVisible(self, label):
        ...
    def _upgradeEquipment(self):
        ...
