# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ExampleDestructible.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lrange as lrange
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from constants import DESTRUCTIBLE_MATKIND as DESTRUCTIBLE_MATKIND

class ExampleDestructible(BigWorld.Entity):
    __MATKINDS_ALL: Any
    __MODEL_NAME: str
    __materialDisabler: Any
    model: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def showDamage(self, componentID, isShotDamage):
        ...
    def set_health(self, prev):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def __onHealthChanged(self):
        ...
