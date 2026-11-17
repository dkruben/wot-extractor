# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/NetworkEntity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV

class NetworkEntity(BigWorld.Entity):
    ignoreEntityGOSync = True
    entityGameObject: Any
    def __init__(self):
        ...
    def onEnterWorld(self, _):
        ...
    def onLeaveWorld(self):
        ...
    @property
    def gameObject(self):
        ...
    @property
    def isConnected(self):
        ...
    def onDynamicComponentCreated(self, component):
        ...
    def onDynamicComponentDestroyed(self, component):
        ...
    @staticmethod
    def __processAddComponent(go, component):
        ...
    @staticmethod
    def __processRemoveComponent(go, component):
        ...
