# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_control/controllers/comp7_vehicle_ban_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from comp7_core_constants import ArenaPrebattlePhase as ArenaPrebattlePhase
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from Event import EventManager as EventManager, Event as Event
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController

class Comp7VehicleBanController(IBattleController):
    __eventsManager: Any
    onVehicleBanStateUpdated: Any
    onCandidatesForBanUpdated: Any
    onBanPhaseUpdated: Any
    __isVehicleBanEnabled: Any
    __vehiclePrepickEndTime: Any
    __vehicleBanEndTime: Any
    __currentPrebattlePhase: Any
    __vehiclesListForBan: Any
    __playersChoiceForBan: Any
    __bannedVehicles: Any
    __candidatesForBan: Any
    __vehicleCopiesInfo: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *_):
        ...
    def stopControl(self):
        ...
    @property
    def isVehicleBanEnabled(self):
        ...
    @property
    def vehiclePrepickEndTime(self):
        ...
    @property
    def vehicleBanEndTime(self):
        ...
    @property
    def vehiclesListForBan(self):
        ...
    @property
    def bannedVehicles(self):
        ...
    @property
    def candidatesForBan(self):
        ...
    @isVehicleBanEnabled.setter
    def isVehicleBanEnabled(self, value):
        ...
    @vehiclePrepickEndTime.setter
    def vehiclePrepickEndTime(self, value):
        ...
    @vehicleBanEndTime.setter
    def vehicleBanEndTime(self, value):
        ...
    @vehiclesListForBan.setter
    def vehiclesListForBan(self, vehiclesList):
        ...
    @bannedVehicles.setter
    def bannedVehicles(self, vehiclesList):
        ...
    @candidatesForBan.setter
    def candidatesForBan(self, candidates):
        ...
    def updatePlayersChoiceForBan(self, playersChoiceForBan):
        ...
    def getPlayerChoiceForBan(self, playerDatabaseID):
        ...
    def updateVehicleCopiesInfo(self, vehicleCopiesInfo):
        ...
    def getVehicleCopies(self, vehicleCD):
        ...
    def chooseVehicleForBan(self, vehicleCD):
        ...
    def confirmBanVehicle(self):
        ...
    def getArenaPrebattlePhase(self):
        ...
    def __updatePhase(self):
        ...
