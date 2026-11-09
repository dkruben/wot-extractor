# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/event_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/techtree/event_helpers.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from helpers.time_utils import getTimeStructInLocal

class TechTreeFormatters(object):

    @staticmethod
    def getActionInfoStr(title, finishTime):
        return backport.text(R.strings.tutorial.techtree.nationDiscount.title(), name=title, time=TechTreeFormatters.__getDateTimeText(finishTime))

    @staticmethod
    def __getDateTimeText(dateTime):
        localDateTime = getTimeStructInLocal(dateTime)
        monthName = backport.text(R.strings.menu.dateTime.months.dyn(('c_{}').format(localDateTime.tm_mon))())
        dateTimeText = backport.text(R.strings.tutorial.techtree.nationDiscount.dateTime(), day=localDateTime.tm_mday, monthName=monthName, year=localDateTime.tm_year)
        return dateTimeText
