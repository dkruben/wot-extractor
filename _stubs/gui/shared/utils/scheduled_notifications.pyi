# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/scheduled_notifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import operator as operator
import BigWorld as BigWorld
from helpers import time_utils as time_utils
from shared_utils import forEach as forEach, findFirst as findFirst
_logger: Any

class Notifiable(object):
    __notificators: Any
    def __init__(self, *args, **kwargs):
        ...
    def addNotificator(self, notificator):
        ...
    def addNotificators(self, *notificators):
        ...
    def startNotification(self):
        ...
    def stopNotification(self):
        ...
    def clearNotification(self):
        ...

class _Notifier(object):
    __deltaFunc: Any
    _updateFunc: Any
    _notificationCallbackID: Any
    def __init__(self, deltaFunc, updateFunc):
        ...
    def clear(self):
        ...
    def startNotification(self):
        ...
    def stopNotification(self):
        ...
    def _getNextNotificationDelta(self, delta):
        ...
    def _registerCallback(self, nextNotification, notificationHandler):
        ...
    def _cancelCallback(self):
        ...
    def _onNotification(self):
        ...
    def __scheduleNextNotification(self):
        ...
    def __cancelNotification(self):
        ...

class PeriodicNotifier(_Notifier):
    __periods: Any
    def __init__(self, deltaFunc, updateFunc, periods=None):
        ...
    def _getNextNotificationDelta(self, delta):
        ...

class DeltaNotifier(_Notifier):
    __delta: Any
    def __init__(self, deltaFunc, updateFunc, delta):
        ...
    def _getNextNotificationDelta(self, delta):
        ...

class SimpleNotifier(_Notifier):
    def _getNextNotificationDelta(self, delta):
        ...

class AcyclicNotifier(SimpleNotifier):
    _notificationCallbackID: Any
    def _onNotification(self):
        ...

class TimerNotifier(_Notifier):
    def _getNextNotificationDelta(self, delta):
        ...
