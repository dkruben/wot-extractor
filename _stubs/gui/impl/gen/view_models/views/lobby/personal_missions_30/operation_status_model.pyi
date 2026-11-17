# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/operation_status_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class OperationStatus(Enum):
    CAMPAIGN_FINISHED = 'campaignFinished'
    NOT_ALL_COMPLETED = 'notAllCompleted'
    NOT_ALL_COMPLETED_WITH_HONOR = 'notAllCompletedWithHonor'
    PAUSED = 'paused'
    NEXT_OPERATION_AVAILABLE = 'nextOperationAvailable'
    COMPLETED = 'completed'
    PRECEDING_OPERATION_NOT_COMPLETED = 'precedingOperationNotCompleted'
    REQUIRES_VEHICLE = 'requiresVehicle'
    VEHICLE_IS_IN_BATTLE = 'vehicleIsInBattle'
    ACTIVE = 'active'
    AVAILABLE = 'available'

class OperationStatusModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def getRequiredVehicleLevel(self):
        ...
    def setRequiredVehicleLevel(self, value):
        ...
    def getCurrentOperationId(self):
        ...
    def setCurrentOperationId(self, value):
        ...
    def getNextOperationName(self):
        ...
    def setNextOperationName(self, value):
        ...
    def getCurrentOperationName(self):
        ...
    def setCurrentOperationName(self, value):
        ...
    def getOperationIdToPerform(self):
        ...
    def setOperationIdToPerform(self, value):
        ...
    def _initialize(self):
        ...
