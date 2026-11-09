# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lobby_state_machine/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lobby_state_machine/events.py
from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent
from gui.shared.events import NavigationEvent

class _BackNavigationEvent(SharedEvent):
    EVENT_ID = 'backNavigationEvent'

    def __init__(self, requestingState=None):
        super(_BackNavigationEvent, self).__init__(eventType=self.EVENT_ID)
        self.requestingState = requestingState


class _BackNavigationGeneratedNavigationEvent(NavigationEvent):

    def __init__(self, targetStateID, params, shouldKillView):
        super(_BackNavigationGeneratedNavigationEvent, self).__init__(targetStateID, params)
        self.shouldKillView = shouldKillView


class _NonViewClosingBackNavigationEvent(_BackNavigationEvent):
    EVENT_ID = 'nonViewClosingBackNavigationEvent'


class _StopEvent(NavigationEvent):
    pass
