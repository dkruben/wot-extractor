# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/backport/backport_time_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_time_utils.py
from __future__ import absolute_import
import time
from gui.impl.backport import text
from helpers import time_utils

def getTillTimeStringByRClass(timeValue, stringRClass, isRoundUp=False, removeLeadingZeros=True):
    gmtime = time.gmtime(timeValue)
    if isRoundUp and gmtime.tm_sec > 0:
        timeValue += time_utils.ONE_MINUTE
        gmtime = time.gmtime(timeValue)
    if timeValue >= time_utils.ONE_DAY:
        fmtKey = 'days'
        gmtime = time.gmtime(timeValue - time_utils.ONE_DAY)
    elif timeValue >= time_utils.ONE_HOUR:
        fmtKey = 'hours'
    elif timeValue >= time_utils.ONE_MINUTE:
        fmtKey = 'min'
    else:
        fmtKey = 'lessMin'
    tm = time.struct_time(gmtime)
    otherYearsdays = (tm.tm_year - 1970) * time_utils.DAYS_IN_YEAR
    fmtValues = {'day': (str(tm.tm_yday + otherYearsdays)), 
       'hour': ((removeLeadingZeros or time.strftime)('%H', gmtime) if 1 else str(tm.tm_hour)), 
       'min': ((removeLeadingZeros or time.strftime)('%M', gmtime) if 1 else str(tm.tm_min)), 
       'sec': (time.strftime('%S', gmtime))}
    return text(stringRClass.dyn(fmtKey)(), **fmtValues)
