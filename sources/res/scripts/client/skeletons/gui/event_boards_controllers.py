# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/event_boards_controllers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/event_boards_controllers.py
from __future__ import absolute_import
import typing
from adisp import adisp_process, adisp_async
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Type
    from gui.event_boards.event_boards_items import IPlayerProgression

class IEventBoardController(object):

    def isElenQuestsStatusWrong(self, currentEvent):
        raise NotImplementedError

    def getPlayerEventsData(self):
        raise NotImplementedError

    def hasEvents(self):
        raise NotImplementedError

    def getEventsSettingsData(self):
        raise NotImplementedError

    def getMyEventsTopData(self):
        raise NotImplementedError

    def getHangarFlagData(self):
        raise NotImplementedError

    def updateHangarFlag(self):
        raise NotImplementedError

    def cleanEventsData(self):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def joinEvent(self, eventID, callback):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def leaveEvent(self, eventID, callback):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getHangarFlag(self, callback, onLogin=False):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getEvents(self, callback, onlySettings=True, isTabVisited=False, onLogin=False, prefetchKeyArtBig=True):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getMyLeaderboardInfo(self, eventID, leaderboardID, callback, showNotification=True):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getLeaderboard(self, eventID, leaderboardID, pageNumber, callback, leaderBoardClass=None, showNotification=True):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getPlayerProgression(self, eventID, leaderboardID, progressionClass, callback=None, showNotification=True):
        raise NotImplementedError
