# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/event_boards/settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/event_boards/settings.py


class _EventBoardSettings(object):

    def __init__(self):
        self.__minimized = {}

    def isGroupMinimized(self, event):
        groupID = event.getEventID()
        if groupID in self.__minimized:
            return self.__minimized[groupID]
        return event.isFinished()

    def updateExpanded(self, event, value):
        groupID = event.getEventID()
        self.__minimized[groupID] = not value


_settings = _EventBoardSettings()

def isGroupMinimized(event):
    return _settings.isGroupMinimized(event)


def expandGroup(event, isExpanded):
    _settings.updateExpanded(event, isExpanded)
