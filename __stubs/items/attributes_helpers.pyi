# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/attributes_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import intern as intern
from future.utils import iteritems as iteritems
from typing import Dict as Dict, Tuple as Tuple, Iterable as Iterable, List as List, TYPE_CHECKING as TYPE_CHECKING
from items import _xml as _xml
import ResMgr as ResMgr
STATIC_ATTR_PREFIX = 'miscAttrs/'
DYNAMIC_ATTR_PREFIX = 'dynAttrs/'
DESCR_MODIFY_ATTR_PREFIX = 'descrAttrs/'
AUTOSHOOT_ATTR_PREFIX = 'autoShootAttrs/'
ALLOWED_STATIC_ATTRS: set
ALLOWED_DYNAMIC_ATTRS: set
AUTOSHOOT_DYNAMIC_ATTRS: set
ALLOWED_ATTRS: dict
ALLOWED_ATTR_PREFIXES: Any

class DescrModifyAttrsCheker(object):
    def __contains__(self, item):
        ...

class MODIFIER_TYPE:
    MUL = 'mul'
    ADD = 'add'
    SET = 'set'

class MODIFIER_FILTER_TYPE:
    COMMON = 'common'
    DEFAULT = 'default'
    SIEGE = 'siege'

class SingleCollectorHelper(object):
    _EMPTY_CHECKER: dict
    _APPLIERS: dict
    @staticmethod
    def isEmpty(opType, value):
        ...
    @staticmethod
    def collect(total, modifiersList, attrPrefix, filter=None):
        ...

class AggregatedCollectorHelper(object):
    _EMPTY_CHECKER: dict
    _MERGERS: dict
    _APPLIERS: dict
    @staticmethod
    def isEmpty(opType, value):
        ...
    @staticmethod
    def collect(total, modifiersList, attrPrefix, filter=None):
        ...

def _parseAttrName(complexName):
    ...
def readModifiers(xmlCtx, section):
    ...
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    ...
def onCollectAttributes(total, modifiersList, attrPrefix, asAggregated, filter=None):
    ...
