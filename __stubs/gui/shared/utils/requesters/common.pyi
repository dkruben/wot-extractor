# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Iterable as Iterable, Any as Any

class RequestProcessor(object):
    __callback: _Any
    __fired: _Any
    __bwCallbackID: _Any
    def __init__(self, delay, callback):
        ...
    @property
    def isFired(self):
        ...
    def cancel(self):
        ...
    def __cooldownCallback(self):
        ...

class BaseDelta(object):
    eventsCache: _Any
    _currValues: _Any
    _prevValues: _Any
    _prevFactory: _Any
    _prevIsInitialized: _Any
    def __init__(self, prevFactory=None):
        ...
    def update(self, data):
        ...
    def updatePrevValueToCurrentValue(self, entryId):
        ...
    def getPrevValue(self, entryId):
        ...
    def clear(self):
        ...
    def hasDiff(self, entryId):
        ...
    def _hasEntryChanged(self, entryId):
        ...
    def _removeOutdatedValues(self):
        ...
    def _getDataIterator(self, data):
        ...
    def _getDefaultValue(self):
        ...
    def _initializePrevValues(self):
        ...
