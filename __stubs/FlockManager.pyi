# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/FlockManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
g_FlockManager = None
_FLOCK_ENABLED = True

class FlockManager(object):
    __flockManager: Any
    __flocks: Any
    def __init__(self):
        ...
    def start(self, player):
        ...
    def stop(self, player):
        ...
    def onSpaceLoaded(self):
        ...
    def onProjectile(self, position):
        ...
    def addFlock(self, position, radius, explosionRadius, respawnTime, flock):
        ...
    def __onVehicleEnter(self, vehicle):
        ...
    def __onVehicleLeave(self, vehicle):
        ...
    def __onTrigger(self, flockId):
        ...

def getManager():
    ...
