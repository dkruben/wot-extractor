# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_calendar_day_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/ranked/ranked_calendar_day_tooltip.py
from __future__ import absolute_import
from gui.impl.gen import R
from helpers import dependency
from gui.shared.tooltips import TOOLTIP_TYPE
from skeletons.gui.game_control import IRankedBattlesController
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip

class RankedCalendarDayTooltip(PeriodicCalendarDayTooltip):
    _RES_ROOT = R.strings.ranked_battles.calendarDay
    _TOOLTIP_TYPE = TOOLTIP_TYPE.RANKED_CALENDAR_DAY
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def _getController(self, *_):
        return self.__rankedController
