# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/entities/DisposableEntity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from Event import EventManager as EventManager, SafeEvent as SafeEvent
_logger: Any

class EntityState(object):
    UNDEFINED = 0
    CREATING = 1
    CREATED = 2
    DISPOSING = 3
    DISPOSED = 4

class DisposableEntity(object):
    __eManager: Any
    onCreate: Any
    onCreated: Any
    onDispose: Any
    onDisposed: Any
    __lcState: Any
    __postponedState: Any
    def __init__(self):
        ...
    def getState(self):
        ...
    def create(self):
        ...
    def validate(self, *args, **kwargs):
        ...
    def _needToBeDisposed(self):
        ...
    def destroy(self):
        ...
    def isDisposed(self):
        ...
    def isCreated(self):
        ...
    def _populate(self):
        ...
    def _invalidate(self, *args, **kwargs):
        ...
    def _dispose(self):
        ...
    def _destroy(self):
        ...
    def __changeStateTo(self, state):
        ...
    def __invalidatePostponedState(self):
        ...
