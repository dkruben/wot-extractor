# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/helpers/server_settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/helpers/server_settings.py
from __future__ import absolute_import
from collections import namedtuple

class AdventCalendarConfig(namedtuple('AdventCalendarConfig', ('isEnabled', 'startDate', 'postEventStartDate',
                                    'postEventEndDate', 'currencies', 'doors', 'doorOpenTokenMask',
                                    'downloadImgUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, startDate=0, doors=[], postEventStartDate=0, postEventEndDate=0, currencies=[], doorOpenTokenMask='', downloadImgUrl='')
        defaults.update(kwargs)
        return super(AdventCalendarConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.items() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @property
    def doorsCount(self):
        return len(self.doors)

    def isSpecialDay(self, dayId):
        return self.doors[dayId - 1].get('isSpecialDay', False)
