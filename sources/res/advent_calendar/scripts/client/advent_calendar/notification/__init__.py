# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/notification/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/notification/__init__.py
from __future__ import absolute_import
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME
from advent_calendar.gui.impl.lobby.feature.notifications.available_doors_view import AvailableDoorsView
from advent_calendar.notification.listeners import DoorsAvailableListener
from advent_calendar.gui.shared.advent_system_factory import collectDoorsAvailableListener
from gui.impl.gen import R
from gui.shared.system_factory import registerNotificationsListeners, registerGamefaceNotifications, ProxyInjection

def registerAdventNotifications():
    registerNotificationsListeners((
     ProxyInjection(collectDoorsAvailableListener, DoorsAvailableListener),))
    registerGamefaceNotifications({ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME: (
                                                         R.views.advent_calendar.mono.lobby.notification_view(), AvailableDoorsView)})
