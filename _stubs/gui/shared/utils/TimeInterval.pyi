# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/TimeInterval.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import weakref as weakref
import BigWorld as BigWorld
from Event import SafeEvent as SafeEvent
from Event import EventManager as EventManager
_logger: Any

class TimeInterval(object):
    __slots__: tuple
    __callbackID: Any
    __interval: Any
    __obj: Any
    __name: Any
    def __init__(self, interval, obj, name):
        ...
    def restart(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def isStarted(self):
        ...
    def __invoke(self):
        ...

class TimeIntervalEvent(SafeEvent):
    __slots__: tuple
    _timeCallback: Any
    __timeInterval: Any
    def __init__(self, interval, timeCallback=None, manager=None):
        ...
    def __iadd__(self, delegate):
        ...
    def __isub__(self, delegate):
        ...
    def hasListeners(self):
        ...
    def clear(self):
        ...
