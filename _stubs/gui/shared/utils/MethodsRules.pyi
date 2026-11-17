# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/MethodsRules.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from types import MethodType as MethodType
from helpers.aop import copy as copy
_logger: Any

class MethodsRules(object):
    __listenersToSkip: Any
    __notificationToDelay: Any
    __delayersProcessed: Any
    __delayerName: Any
    class delayable(object):
        __delayerName: Any
        def __init__(self, delayerName=None):
            ...
        def __call__(self, listener):
            ...
        def __get__(self, obj, objtype=None):
            ...
    def __init__(self):
        ...
    def clear(self, leave=True):
        ...
    def skipListenerNotification(self, wrapper):
        ...
    def isSkipable(self, listener):
        ...
    def isDelayerProcessed(self, delayerName):
        ...
    def skip(self, listener):
        ...
    def delay(self, delayerName, notification, *args, **kwargs):
        ...
    def processDelayer(self, delayerName):
        ...
