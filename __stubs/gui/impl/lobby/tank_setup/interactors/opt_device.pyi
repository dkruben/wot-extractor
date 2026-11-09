# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/interactors/opt_device.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import adisp as adisp
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback
from BWUtil import AsyncReturn as AsyncReturn
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.tank_setup.interactors.base import BaseInteractor as BaseInteractor
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID
from gui.shared.event_dispatcher import showTankSetupExitConfirmDialog as showTankSetupExitConfirmDialog
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
ActionsFactory: Any

# gerado do bytecode: classes base desconhecidas
class BaseOptDeviceInteractor:
    __slots__: Any
    def getName(self):
        ...
    def affectsTTC(self):
        ...
    def getInstalledLayout(self):
        ...
    def getCurrentLayout(self):
        ...
    def getSetupLayout(self):
        ...
    def getCurrentCategories(self, slotID):
        ...

# gerado do bytecode: classes base desconhecidas
class OptDeviceInteractor:
    __slots__: Any
    _OptDeviceInteractor__canInstall: Any
    def getVehicleAfterInstall(self):
        ...
    def setItemInCurrentLayout(self, slotID, item):
        ...
    def demountProcess(self, slotID, isDestroy=..., isFitting=..., everywhere=..., callback=...):
        ...
    def deconstructProcess(self, slotID, callback=...):
        ...
    def changeSlotItem(self, slotID, itemIntCD):
        ...
    def swapSlots(self, leftID, rightID, actionType=...):
        ...
    def demountItem(self, itemIntCD, isDestroy=..., everywhere=...):
        ...
    def revert(self):
        ...
    def confirm(self, callback, skipDialog=...):
        ...
    def upgradeModule(self, itemIntCD, onDeconstructed, callback):
        ...
    def updateFrom(self, vehicle, onlyInstalled=...):
        ...
    def showExitConfirmDialog(self):
        ...
    def updateAmmunitionPanelChangedItems(self):
        ...
    def __canInstall(self, item, vehicle):
        ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
