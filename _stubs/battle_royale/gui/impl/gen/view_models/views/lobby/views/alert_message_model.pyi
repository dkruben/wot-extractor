# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/alert_message_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Map as Map, ViewModel as ViewModel

class AlertType(Enum):
    NONE = 'none'
    CEASEFIRECURRENTSERVER = 'ceasefireCurrentServer'
    CEASEFIREALLSERVERS = 'ceasefireAllServers'
    MODEISUNAVAILABLE = 'modeIsUnavailable'
    MODEISFINISHED = 'modeIsFinished'

class AlertMessageModel(ViewModel):
    __slots__: tuple
    onChangeServer: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getAlertType(self):
        ...
    def setAlertType(self, value):
        ...
    def getBattleSchedule(self):
        ...
    def setBattleSchedule(self, value):
        ...
    @staticmethod
    def getBattleScheduleType():
        ...
    def _initialize(self):
        ...
