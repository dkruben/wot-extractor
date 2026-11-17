# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/ClientPrebattle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.moves import pickle as pickle
import Event as Event
from constants import PREBATTLE_UPDATE as PREBATTLE_UPDATE, PREBATTLE_TEAM_STATE as PREBATTLE_TEAM_STATE
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV

class ClientPrebattle(object):
    __onUpdate: dict
    id: Any
    settings: Any
    properties: Any
    rosters: Any
    teamStates: Any
    __eventManager: Any
    onRosterReceived: Any
    onPlayerAdded: Any
    onPlayerRemoved: Any
    onPlayerStateChanged: Any
    onPlayerGroupChanged: Any
    onPlayerRosterChanged: Any
    onTeamStatesReceived: Any
    onSettingsReceived: Any
    onSettingUpdated: Any
    onKickedFromQueue: Any
    onPropertiesReceived: Any
    onPropertyUpdated: Any
    def __init__(self, prebattleID):
        ...
    def destroy(self):
        ...
    def update(self, updateType, argStr):
        ...
    def __accInfoAsDict(self, accInfoAsTuple):
        ...
    def __onRosterReceived(self, argStr):
        ...
    def __onPlayerAdded(self, argStr):
        ...
    def __onPlayerRemoved(self, argStr):
        ...
    def __onPlayerStateChanged(self, argStr):
        ...
    def __onPlayerRosterChanged(self, argStr):
        ...
    def __onPlayerGroupChanged(self, argStr):
        ...
    def __onTeamStatesReceived(self, argStr):
        ...
    def __onSettingsReceived(self, argStr):
        ...
    def __onSettingUpdated(self, argStr):
        ...
    def __onPropertiesReceived(self, argStr):
        ...
    def __onPropertyUpdated(self, argStr):
        ...
    def __onKickedFromQueue(self, argStr):
        ...
