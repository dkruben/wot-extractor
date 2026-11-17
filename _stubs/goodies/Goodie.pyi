# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/Goodie.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from itertools import chain as chain
from future.utils import viewitems as viewitems
from typing import Dict as Dict, Tuple as Tuple
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from goodies.goodie_constants import GOODIE_STATE as GOODIE_STATE

class Goodie(object):
    __slots__: list
    uid: Any
    state: Any
    finishTime: Any
    counter: Any
    expirations: Any
    def __init__(self, uid, state=..., finishTime=0, counter=0, expirations=None):
        ...
    def __repr__(self):
        ...
    def isActive(self):
        ...
    def isEffectFinished(self):
        ...
    def isExpirable(self):
        ...
    def isExpired(self):
        ...
    def splitExpirations(self):
        ...
    def toPdata(self):
        ...

def decrementExpirationsInOrder(amountToRemove, oldExpirations):
    ...
def mergeExpirationsInto(source, target):
    ...
