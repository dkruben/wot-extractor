# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/trajectory_drawer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION

class TrajectoryDrawer(object):
    __slots__: tuple
    __impl: Any
    def __init__(self, spaceID):
        ...
    def destroy(self):
        ...
    def addProjectile(self, shotID, attackerID, startPoint, velocity, gravity, maxDistance, isOwnShot):
        ...
    def removeProjectile(self, shotID):
        ...

class _TrajectoryDrawerImpl(object):
    __slots__: tuple
    __spaceID: Any
    __isEnabled: Any
    __gameObject: Any
    __drawer: Any
    def __init__(self, spaceID):
        ...
    def destroy(self):
        ...
    def addProjectile(self, shotID, attackerID, startPoint, velocity, gravity, maxDistance, isOwnShot):
        ...
    def removeProjectile(self, shotID):
        ...
    @staticmethod
    def __castBool(value):
        ...
    def __getEnabled(self):
        ...
    def __setEnabled(self, value):
        ...
