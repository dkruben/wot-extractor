# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/notification_commands.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from frameworks.wulf import WindowStatus as WindowStatus
from gui.Scaleform.framework.entities.sf_window import SFWindow as SFWindow
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from typing import Any as Any

class NotificationEvent(object):
    __slots__: tuple
    _method: _Any
    _args: _Any
    _kwargs: _Any
    def __init__(self, method, *args, **kwargs):
        ...
    def __call__(self):
        ...
    def isEventSet(self):
        ...

class NotificationCommand(object):
    __slots__: tuple
    __hash__ = None
    isPersistent = True
    def __eq__(self, other):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def execute(self):
        ...
    def getWindow(self):
        ...

class WindowNotificationCommand(NotificationCommand):
    __slots__: tuple
    __hash__ = None
    __window: _Any
    def __init__(self, window):
        ...
    def __eq__(self, other):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def execute(self):
        ...
    def getWindow(self):
        ...

class EventNotificationCommand(NotificationCommand):
    __slots__: tuple
    __hash__ = None
    __event: _Any
    def __init__(self, event):
        ...
    def __eq__(self, other):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def execute(self):
        ...
    def getWindow(self):
        ...
    def getEvent(self):
        ...

class NonPersistentEventNotificationCommand(EventNotificationCommand):
    __slots__: tuple
    isPersistent = False
