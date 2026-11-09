# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/AdventCalendarPersonality.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/AdventCalendarPersonality.py
from __future__ import absolute_import
from advent_calendar.gui.Scaleform import registerAdventCalendarScaleform
from advent_calendar.messenger import registerAdventCalendarTokenQuestsSubFormatters
from advent_calendar.notification import registerAdventNotifications
from advent_calendar.skeletons import registerAdventCalendarController

def preInit():
    registerAdventCalendarController()
    registerAdventCalendarScaleform()
    registerAdventCalendarTokenQuestsSubFormatters()
    registerAdventNotifications()


def init():
    pass


def start():
    pass


def fini():
    pass
