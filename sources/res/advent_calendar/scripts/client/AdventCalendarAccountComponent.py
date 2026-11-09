# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/AdventCalendarAccountComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/AdventCalendarAccountComponent.py
from __future__ import absolute_import
import typing
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from advent_calendar_common import advent_calendar_account_commands
if typing.TYPE_CHECKING:
    from typing import Callable, Optional

class AdventCalendarAccountComponent(BaseAccountExtensionComponent):

    def openAdventCalendarDoor(self, dayID, currency='', callback=None):
        proxy = (lambda requestID, resultID, errorStr: callback(resultID, errorStr)) if callback is not None else None
        self.account._doCmdIntStr(advent_calendar_account_commands.CMD_OPEN_ADVENT_CALENDAR_DOOR, dayID, currency, proxy)
        return
