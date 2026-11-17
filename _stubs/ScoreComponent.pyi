# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/ScoreComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import wraps as wraps
import BigWorld as BigWorld
import Event as Event
from constants import ARENA_PERIOD as ARENA_PERIOD
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak

class ScoreComponent(DynamicScriptComponent):
    onTeamsScoreUpdated: Any
    onPersonalScoreUpdated: Any
    _pendingEvents: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    # decorador original: @delayEventWrapper(...)
    def set_teamScore(self, _):
        ...
    # decorador original: @delayEventWrapper(...)
    def set_vehiclesScore(self, _):
        ...
    def scheduleEvent(self, eventName, propertyName):
        ...
    def _sendPendingEvents(self):
        ...

def delayEventWrapper(eventName, propertyName):
    ...
