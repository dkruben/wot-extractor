# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tank_setup/interactor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.impl.lobby.tank_setup.interactors.consumable import ConsumableInteractor as ConsumableInteractor
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from adisp import adisp_process as adisp_process
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants as LSTankSetupConstants
from gui.shared.gui_items.processors import Processor as Processor
from gui.shared.utils import decorators as decorators
from gui.impl.lobby.tank_setup.interactors.base import BaseAutoRenewal as BaseAutoRenewal
from LSAccountEquipmentController import getLSConsumables as getLSConsumables

class ActionTypes(object):
    BUY_AND_INSTALL_LS_CONSUMABLES_ACTION = 'buyAndInstallLSConsumables'

class LSConsumableInteractor(ConsumableInteractor):
    CONFIRM_ACTION = ActionTypes.BUY_AND_INSTALL_LS_CONSUMABLES_ACTION
    _playerLayout: Any
    def getName(self):
        ...
    # decorador original: @adisp_process
    def confirm(self, callback, skipDialog=False):
        ...
    def getInstalledLayout(self):
        ...
    def getCurrentLayout(self):
        ...
    def getVehicleAfterInstall(self):
        ...
    def revert(self):
        ...
    def updateFrom(self, vehicle, onlyInstalled=True):
        ...
    def _createAutoRenewal(self):
        ...

class LSVehicleAutoEquipProcessor(Processor):
    _value: Any
    _vehicle: Any
    def __init__(self, vehicle, value):
        ...
    def _request(self, callback):
        ...

class LSConsumableAutoRenewal(BaseAutoRenewal):
    def getValue(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def processVehicleAutoRenewal(self, callback):
        ...
