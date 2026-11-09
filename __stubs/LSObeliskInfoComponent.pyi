# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSObeliskInfoComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from Event import Event as Event
from helpers import isPlayerAvatar as isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class ObeliskInfoStates(object):
    SHOW = 'show'
    HIT = 'hit'
    DEATH = 'death'
    HIDE = 'hide'

class LSObeliskInfoComponent(DynamicScriptComponent):
    onStateChange: Any
    onObeliskObserved: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def set_isPresent(self, _):
        ...
    def set_observedObeliskCD(self, _):
        ...
    def onDamageReceived(self):
        ...
    def onDeath(self):
        ...
    @staticmethod
    def getInstance():
        ...
    def _onAvatarReady(self):
        ...
