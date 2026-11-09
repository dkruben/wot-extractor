# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/events_notifications.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/events_notifications.py
from __future__ import absolute_import
from builtins import map
from collections import namedtuple
from future.utils import lfilter, lmap
import BigWorld, Event
from PlayerEvents import g_playerEvents
from helpers import getLocalizedData
from skeletons.gui.game_control import IEventsNotificationsController

class EventsNotificationsController(IEventsNotificationsController):

    def __init__(self):
        super(EventsNotificationsController, self).__init__()
        self.__eventMgr = Event.EventManager()
        self.onEventNotificationsChanged = Event.Event(self.__eventMgr)

    def fini(self):
        self.__stop()
        self.__eventMgr = None
        super(EventsNotificationsController, self).fini()
        return

    def onLobbyInited(self, event):
        g_playerEvents.onEventNotificationsChanged += self.__onEventNotification

    def onAvatarBecomePlayer(self):
        self.__stop()

    def onDisconnected(self):
        self.__stop()

    def getEventsNotifications(self, filterFunc=None):
        player = BigWorld.player()
        if player:
            return lfilter(filterFunc or (lambda a: True), map(EventNotification.make, player.eventNotifications))
        return ()

    def __stop(self):
        self.__eventMgr.clear()
        g_playerEvents.onEventNotificationsChanged -= self.__onEventNotification

    def __onEventNotification(self, diff):
        added = lmap(EventNotification.make, diff.get('added', ()))
        removed = lmap(EventNotification.make, diff.get('removed', ()))
        self.onEventNotificationsChanged(added, removed)


class EventNotification(namedtuple('EventNotification', 'eventType data text')):

    @classmethod
    def default(cls):
        return cls.__new__(cls, None, None, None)

    @classmethod
    def make(cls, data):
        text = getLocalizedData(data, 'text')
        return cls.__new__(cls, data['type'], data.get('data'), text)
