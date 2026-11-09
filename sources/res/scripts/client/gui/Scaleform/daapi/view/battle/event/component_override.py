# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/component_override.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/component_override.py
from __future__ import absolute_import
from gui.battle_control import avatar_getter
from constants import ARENA_GUI_TYPE

class EventComponentOverride(object):
    __slots__ = ('__usualObject', '__eventObject')

    def __init__(self, usualObject, eventObject):
        super(EventComponentOverride, self).__init__()
        self.__usualObject = usualObject
        self.__eventObject = eventObject

    def __call__(self):
        arena = avatar_getter.getArena()
        isEvent = arena.guiType == ARENA_GUI_TYPE.EVENT_BATTLES if arena else False
        if isEvent:
            return self.__eventObject
        return self.__usualObject
