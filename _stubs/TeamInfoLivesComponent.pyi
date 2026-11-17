# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TeamInfoLivesComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
from helpers import isPlayerAvatar as isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class TeamInfoLivesComponent(DynamicScriptComponent):
    onTeamLivesUpdated: Any
    def __init__(self, *_, **__):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_teamLives(self, prev):
        ...
    def getLives(self, vehicleID):
        ...
    def getLockedLives(self, vehicleID):
        ...
    def getUsedLives(self, vehicleID):
        ...
    def getVehicleLives(self, vehicleID):
        ...
    @classmethod
    def getInstance(cls):
        ...
