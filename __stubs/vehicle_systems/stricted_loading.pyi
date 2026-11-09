# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/stricted_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import weakref as weakref
import functools as functools
import inspect as inspect
import BigWorld as BigWorld
import debug_utils as debug_utils
from constants import IS_EDITOR as IS_EDITOR
_MAX_PRIORITY = 96
_HIGH_PRIORITY = 128
_LOG_LEAKS = False
_LOG_MSG = 'Prevented possible leak of callback!'

def loadingPriority(vehicleID):
    ...
def restrictBySpace(callback, *args, **kwargs):
    ...
def restrictBySpaceAndNode(node, callback, *args, **kwargs):
    ...
def _restrictedLoadCall(spaceID, node, callback, resource, args, kwargs):
    ...
def makeCallbackWeak(callback, *args, **kwargs):
    ...
def _weakMethodCall(selfWeak, methodWeak, predefArgs, predefKwargs, *args, **kwargs):
    ...
def _weakCall(callbackWeak, predefArgs, predefKwargs, *args, **kwargs):
    ...
