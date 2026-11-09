# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/skeletons/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/skeletons/__init__.py
from __future__ import absolute_import
from advent_calendar.gui.game_control.advent_calendar_controller import AdventCalendarController
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from gui.shared.system_factory import registerGameControllers

def registerAdventCalendarController():
    registerGameControllers([
     (
      IAdventCalendarController, AdventCalendarController, False)])
