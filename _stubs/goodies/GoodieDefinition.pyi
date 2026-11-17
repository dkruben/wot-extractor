# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/GoodieDefinition.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from typing import TYPE_CHECKING as TYPE_CHECKING
from future.utils import viewvalues as viewvalues
from goodies.Goodie import Goodie as Goodie
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY, GOODIE_STATE as GOODIE_STATE
from soft_exception import SoftException as SoftException
from typing import Optional as Optional, Dict as Dict
from goodies.GoodieConditions import GoodieConditionType as GoodieConditionType
from goodies.GoodieTargets import GoodieTargetType as GoodieTargetType
from goodies.GoodieValue import GoodieValueType as GoodieValueType
from goodies.GoodieResources import GoodieResourceType as GoodieResourceType

class OverLimitException(SoftException):
    ...

class ExpirationCountException(SoftException):
    def __init__(self, state):
        ...

class GoodieDefinition(object):
    __slots__: list
    uid: Any
    variety: Any
    target: Any
    enabled: Any
    lifetime: Any
    useby: Any
    counter: Any
    autostart: Any
    resource: Any
    value: Any
    condition: Any
    expireAfter: Any
    roundToEndOfGameDay: Any
    def __init__(self, uid, variety, target, enabled, lifetime, useby, counter, autostart, resource, value, condition, expireAfter, roundToEndOfGameDay):
        ...
    def __repr__(self):
        ...
    def isActivatable(self):
        ...
    def isExpirable(self):
        ...
    def isTimeLimited(self):
        ...
    def isCountable(self):
        ...
    def isPastUseBy(self):
        ...
    def apply(self, resources, applyToZero):
        ...
    def apply_delta(self, resource, applyToZero):
        ...
    def createGoodie(self, state=None, finishTime=None, counter=None, expirations=None):
        ...
    def createDisabledGoodie(self, counter, expirations):
        ...
