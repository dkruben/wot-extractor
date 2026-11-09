# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_calendar_day_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_calendar_day_tooltip.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.shared.tooltips import TOOLTIP_TYPE
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip
from helpers import dependency
from skeletons.gui.game_control import IMapboxController

class MapboxCalendarDayTooltip(PeriodicCalendarDayTooltip):
    _controller = dependency.descriptor(IMapboxController)
    _TOOLTIP_TYPE = TOOLTIP_TYPE.MAPBOX_CALENDAR_DAY
    _RES_ROOT = R.strings.mapbox.calendarDay

    def _getController(self, *_):
        return self._controller

    def _isValidPrimeTimes(self, serversPeriodsMapping):
        allPeriods = [periods for serverPeriods in serversPeriodsMapping.values() for periods in serverPeriods]
        return len(allPeriods) > 0
