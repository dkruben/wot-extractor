# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarCommendations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import AccountCommands as AccountCommands
from Event import Event as Event
from constants import CommendationsState as CommendationsState
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from typing import Dict as Dict, List as List
from commendations_common.CommendationHelpers import CommendationStateType as CommendationStateType, CommendationsSource as CommendationsSource
_logger: Any

class AvatarCommendations(DynamicScriptComponent):
    _messageStateMap: Any
    onStateUpdate: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def set_commendationsState(self, oldState):
        ...
    def setNested_commendationsState(self, path, oldState):
        ...
    def updateMessageStateMap(self):
        ...
    def getMessageStateForVehID(self, vehID):
        ...
    def sendCommendation(self, recipientID, source):
        ...
    def clearMessageState(self, callback=None):
        ...
