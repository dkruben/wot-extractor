# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/prebattle_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel

class PrebattleModel(ViewModel):
    __slots__: tuple
    PLAYER_CREATOR = 'playerCreator'
    PLAYER_READY = 'playerReady'
    READINESS_AVAILABLE = 'readinessAvailable'
    ACTION_ENABLED = 'actionEnabled'
    BATTLE_START_ACTION_TYPE = 'battleStartAction'
    BATTLE_READY_ACTION_TYPE = 'readyAction'
    BATTLE_EXIT_ACTION_TYPE = 'battleExitAction'
    BATTLE_STATE_IDLE = 'idle'
    BATTLE_STATE_SEARCHING = 'searchingBattle'
    BATTLE_STATE_READY = 'battleReady'
    E_SPORT = 'E_SPORT'
    TRAINING = 'TRAINING'
    BATTLE_SESSION = 'BATTLE_SESSION'
    RANDOM = 'RANDOM'
    EVENT = 'EVENT'
    STRONGHOLD = 'STRONGHOLD'
    RANKED = 'RANKED'
    EPIC_TRAINING = 'EPIC_TRAINING'
    TOURNAMENT = 'TOURNAMENT'
    EPIC = 'EPIC'
    BATTLE_ROYALE = 'BATTLE_ROYALE'
    MAPBOX = 'MAPBOX'
    MAPS_TRAINING = 'MAPS_TRAINING'
    BATTLE_ROYALE_TOURNAMENT = 'BATTLE_ROYALE_TOURNAMENT'
    onAction: Any
    def __init__(self, properties=7, commands=1):
        ...
    @property
    def battleVehicle(self):
        ...
    @staticmethod
    def getBattleVehicleType():
        ...
    def getStates(self):
        ...
    def setStates(self, value):
        ...
    @staticmethod
    def getStatesType():
        ...
    def getCurrentMode(self):
        ...
    def setCurrentMode(self, value):
        ...
    def getCurrentModeId(self):
        ...
    def setCurrentModeId(self, value):
        ...
    def getQueueType(self):
        ...
    def setQueueType(self, value):
        ...
    def getBattleStatus(self):
        ...
    def setBattleStatus(self, value):
        ...
    def getBattleButtonAlwaysOn(self):
        ...
    def setBattleButtonAlwaysOn(self, value):
        ...
    def _initialize(self):
        ...
