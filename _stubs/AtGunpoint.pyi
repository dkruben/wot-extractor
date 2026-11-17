# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AtGunpoint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from math_utils import almostZero as almostZero
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
ARTY_HIT_PREDICTION_EPSILON_YAW = 1e-05

class AtGunpoint(BigWorld.DynamicScriptComponent):
    __guiSessionProvider: Any
    def __init__(self):
        ...
    def _avatar(self):
        ...
    def onDestroy(self):
        ...
    def setSlice_attackers(self, path, prev):
        ...
    def __isSameYaw(self, a, b):
        ...
