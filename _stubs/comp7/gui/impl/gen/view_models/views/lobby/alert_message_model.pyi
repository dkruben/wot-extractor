# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/alert_message_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class State(Enum):
    NONE = 'none'
    BAN = 'ban'
    PREANNOUNCE = 'preannounce'
    NOVEHICLES = 'noVehicles'
    NOTENOUGHVEHICLES = 'notEnoughVehicles'
    QUALIFICATION = 'qualification'
    CEASEFIREAVAILABLE = 'ceasefireAvailable'
    CEASEFIREUNAVAILABLE = 'ceasefireUnavailable'
    MODEOFFLINE = 'modeOffline'
    SEASONEND = 'seasonEnd'

class AlertMessageModel(ViewModel):
    __slots__: tuple
    onClick: Any
    def __init__(self, properties=5, commands=1):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getBanTimeleftInSeconds(self):
        ...
    def setBanTimeleftInSeconds(self, value):
        ...
    def getStartEventDateTime(self):
        ...
    def setStartEventDateTime(self, value):
        ...
    def getLevels(self):
        ...
    def setLevels(self, value):
        ...
    @staticmethod
    def getLevelsType():
        ...
    def getMinVehiclesRequired(self):
        ...
    def setMinVehiclesRequired(self, value):
        ...
    def _initialize(self):
        ...
