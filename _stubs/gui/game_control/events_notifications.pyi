# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/events_notifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import map as map
from collections import namedtuple as namedtuple
from future.utils import lfilter as lfilter, lmap as lmap
import BigWorld as BigWorld
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import getLocalizedData as getLocalizedData
from skeletons.gui.game_control import IEventsNotificationsController as IEventsNotificationsController

class EventsNotificationsController(IEventsNotificationsController):
    __eventMgr: Any
    onEventNotificationsChanged: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def getEventsNotifications(self, filterFunc=None):
        ...
    def __stop(self):
        ...
    def __onEventNotification(self, diff):
        ...

# base nao representavel no stub: namedtuple(...)
class EventNotification:
    @classmethod
    def default(cls):
        ...
    @classmethod
    def make(cls, data):
        ...
