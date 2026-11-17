# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/callable_delayer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from Event import Event as Event
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks.wulf import View as WulfView
from gui.Scaleform.framework.entities.View import View as View
from _weakref import ReferenceType as ReferenceType

class CallableDelayer(object):
    __wrappers: Any
    __eventRef: Any
    __wrappedFn: Any
    __cleanupCallback: Any
    class _CleanupWrapper(object):
        __eventRef: Any
        __wrappedFn: Any
        __cleanupCallback: Any
        def __init__(self, eventRef, wrappedFn, cleanupCallback):
            ...
        def __del__(self):
            ...
        def __call__(self):
            ...
        def clear(self):
            ...
    def __init__(self):
        ...
    def __del__(self):
        ...
    def delayUntilEvent(self, event, fn):
        ...
    def clear(self):
        ...
    def __removeWrapper(self, wrapper):
        ...

def delayUntilParentWindowReady(delayer, view, fn):
    ...
