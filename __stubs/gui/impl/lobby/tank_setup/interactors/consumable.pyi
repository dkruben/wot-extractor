# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/interactors/consumable.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from wg_async import wg_async as wg_async, await_callback as await_callback
from gui import shop as shop
from adisp import adisp_process as adisp_process
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.interactors.base import BaseAutoRenewal as BaseAutoRenewal
from gui.impl.lobby.tank_setup.interactors.base_equipment import BaseEquipmentInteractor as BaseEquipmentInteractor
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.shared.gui_items.processors.vehicle import VehicleAutoEquipProcessor as VehicleAutoEquipProcessor
from gui.shared.utils import decorators as decorators

class ConsumableAutoRenewal(BaseAutoRenewal):
    def getValue(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def processVehicleAutoRenewal(self, callback):
        ...

class BaseConsumableInteractor(BaseEquipmentInteractor):
    __slots__: tuple
    def getName(self):
        ...
    def getInstalledLayout(self):
        ...
    def getCurrentLayout(self):
        ...
    def getSetupLayout(self):
        ...

class ConsumableInteractor(BaseConsumableInteractor):
    __slots__: tuple
    _playerLayout: Any
    def getVehicleAfterInstall(self):
        ...
    def revert(self):
        ...
    # decorador original: @wg_async
    def applyQuit(self, callback, skipApplyAutoRenewal):
        ...
    # decorador original: @adisp_process
    def confirm(self, callback, skipDialog=False):
        ...
    def buyMore(self, itemCD):
        ...
    def updateFrom(self, vehicle, onlyInstalled=True):
        ...
    def _createAutoRenewal(self):
        ...
