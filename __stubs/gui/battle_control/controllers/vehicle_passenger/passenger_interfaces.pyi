# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from Event import LateEvent as LateEvent, Event as Event

class IVehiclePassengerWatcher(object):
    @classmethod
    def getVehiclePassengerCtrl(cls):
        ...

class IVehiclePassengerController(IBattleController):
    onVehiclePassengerUpdating = None
    onVehiclePassengerUpdate = None
    @property
    def isCurrentPlayerVehicle(self):
        ...
    @property
    def isCurrentVehicleAlive(self):
        ...
    @property
    def isCurrentVehicleFPV(self):
        ...
    @property
    def currentVehicleID(self):
        ...
    @property
    def playerVehicleID(self):
        ...
    def setPlayerVehicle(self, vehicleID):
        ...
