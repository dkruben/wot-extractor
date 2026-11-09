# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/tooltips/calendar_day_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/tooltips/calendar_day_tooltip.py
from __future__ import absolute_import
from future.utils import viewvalues
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.shared.tooltips import TOOLTIP_TYPE
from gui.impl.gen import R
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip
from helpers.time_utils import ONE_DAY

class FunRandomCalendarDayTooltip(PeriodicCalendarDayTooltip, FunSubModesWatcher):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.FUN_RANDOM
    _RES_ROOT = R.strings.fun_random.calendarDay

    def _getController(self, *_):
        return self.getDesiredSubMode()


class FunRandomModeSelectorCalendarTooltip(FunRandomCalendarDayTooltip):

    def _getController(self, subModeID=None, *_):
        if subModeID is None:
            return self._funRandomCtrl.subModesInfo
        else:
            return self.getSubMode(subModeID)

    def _isValidPrimeTimes(self, serversPeriodsMapping):
        periods = (periods for serverPeriods in viewvalues(serversPeriodsMapping) for periods in serverPeriods)
        return any(period[1] - period[0] != ONE_DAY for period in periods)
