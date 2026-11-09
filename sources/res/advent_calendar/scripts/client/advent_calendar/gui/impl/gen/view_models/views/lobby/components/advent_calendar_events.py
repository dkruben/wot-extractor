# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/components/advent_calendar_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/components/advent_calendar_events.py
from enum import Enum
from frameworks.wulf import ViewModel

class EventType(Enum):
    OPEN_DOOR = 'openDoor'


class AdventCalendarEvents(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(AdventCalendarEvents, self).__init__(properties=properties, commands=commands)

    def getEventType(self):
        return EventType(self._getString(0))

    def setEventType(self, value):
        self._setString(0, value.value)

    def getPayload(self):
        return self._getString(1)

    def setPayload(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(AdventCalendarEvents, self)._initialize()
        self._addStringProperty('eventType', EventType.OPEN_DOOR.value)
        self._addStringProperty('payload', '')
