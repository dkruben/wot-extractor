# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_ctx_notifiers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
NotifySysMessages: Any

class BaseNotifier(object):
    __slots__: tuple
    def getPath(self):
        ...

class SimpleSysMessageNotifier(BaseNotifier):
    __slots__: tuple
    __path: Any
    __states: Any
    def __init__(self, path, states):
        ...
    def __call__(self, nextValue, currentValue):
        ...
    def getPath(self):
        ...
