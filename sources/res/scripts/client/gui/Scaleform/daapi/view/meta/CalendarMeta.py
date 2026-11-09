# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/CalendarMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CalendarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalendarMeta(BaseDAAPIComponent):

    def onMonthChanged(self, rawDate):
        self._printOverrideError('onMonthChanged')

    def onDateSelected(self, rawDate):
        self._printOverrideError('onDateSelected')

    def formatYMHeader(self, rawDate):
        self._printOverrideError('formatYMHeader')

    def as_openMonthS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_openMonth(rawDate)

    def as_selectDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_selectDate(rawDate)

    def as_setMinAvailableDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_setMinAvailableDate(rawDate)

    def as_setMaxAvailableDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxAvailableDate(rawDate)

    def as_setHighlightedDaysS(self, hightlightedTimestamps):
        if self._isDAAPIInited():
            return self.flashObject.as_setHighlightedDays(hightlightedTimestamps)

    def as_setDayTooltipTypeS(self, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setDayTooltipType(tooltipType)
