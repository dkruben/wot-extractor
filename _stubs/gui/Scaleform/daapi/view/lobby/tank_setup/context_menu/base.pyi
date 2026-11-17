# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/context_menu/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import ContextMenu as ContextMenu, CMLabel as CMLabel
from gui.Scaleform.framework.managers.context_menu import CM_BUY_COLOR as CM_BUY_COLOR
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.tank_setup.interactors.base import BaseInteractor as BaseInteractor
FIRST_SLOT = 0
SECOND_SLOT = 1
THIRD_SLOT = 2

class TankSetupCMLabel(object):
    DEMOUNT = 'demount'
    DEMOUNT_FROM_SETUP = 'demountFromSetup'
    DEMOUNT_FROM_SETUPS = 'demountFromSetups'
    DESTROY = 'destroy'
    SELECT = 'select'
    PUT_ON_FIRST = 'putOnFirst'
    PUT_ON_SECOND = 'putOnSecond'
    PUT_ON_THIRD = 'putOnThird'
    TAKE_OFF = 'takeOff'
    UNLOAD = 'unload'
    PUT_ON_LIST: tuple

class ITankSetupCMHandler(object):
    def getSelectedSetup(self):
        ...
    def getVehicleItem(self):
        ...
    def setLastSlotAction(self, *args, **kwargs):
        ...
    def sendSlotAction(self, args):
        ...

class BaseTankSetupContextMenu(ContextMenu):
    _gui: Any
    _itemsCache: Any
    __emitterUID: Any
    _intCD: Any
    _slotType: Any
    _installedSlotId: Any
    _itemInstalledSetupIdx: Any
    _itemInstalledSetupSlotIdx: Any
    _isMounted: Any
    _isMountedMoreThanOne: Any
    _slotsCount: Any
    def _sendSlotAction(self, actionType, **kwargs):
        ...
    def _sendLastSlotAction(self, setupName, actionType, kwargs):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _getEmitterView(self):
        ...
    def _getVehicle(self):
        ...
    def _getCopyVehicle(self):
        ...
    def _getItem(self):
        ...
    def _getVehicleItems(self):
        ...
    def _isInstalledInCurrentLayout(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def _isVisible(self, label):
        ...

class BaseItemContextMenu(BaseTankSetupContextMenu):
    _isDisabled: Any
    def _sendPutOnSlotAction(self, onId):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _getOptionCustomData(self, label):
        ...
    def _isVisible(self, label):
        ...

class BaseSlotContextMenu(BaseTankSetupContextMenu):
    def _sendPutOnSlotAction(self, onId):
        ...
    def _isItemInInventory(self):
        ...
    def _isItemInOtherLayout(self):
        ...
    def _isVisible(self, label):
        ...
