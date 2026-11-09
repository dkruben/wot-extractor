# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/backport/backport_system_locale.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_system_locale.py
from __future__ import absolute_import
from frameworks import wulf

def getIntegralFormat(value):
    return wulf.getNumberFormat(int(value), wulf.NumberFormatType.INTEGRAL)


def getGoldFormat(value):
    return wulf.getNumberFormat(int(value), wulf.NumberFormatType.GOLD)


def getFractionalFormat(value):
    return wulf.getRealFormat(value, wulf.RealFormatType.FRACTIONAL, 2)


def getNiceNumberFormat(value):
    return wulf.getRealFormat(value, wulf.RealFormatType.WO_ZERO_DIGITS, 2)


def getShortTimeFormat(value):
    return wulf.getTimeFormat(value, wulf.TimeFormatType.SHORT_FORMAT)


def getLongTimeFormat(value):
    return wulf.getTimeFormat(value, wulf.TimeFormatType.LONG_FORMAT)


def getShortDateFormat(value):
    return wulf.getDateFormat(value, wulf.DateFormatType.SHORT_FORMAT)


def getLongDateFormat(value):
    return wulf.getDateFormat(value, wulf.DateFormatType.LONG_FORMAT)


def getYearMonthFormat(value):
    return wulf.getDateFormat(value, wulf.DateFormatType.YEAR_MONTH)


def getDateTimeFormat(value):
    return (u'{0:>s} {1:>s}').format(wulf.getDateFormat(value, wulf.DateFormatType.LONG_FORMAT), wulf.getTimeFormat(value, wulf.TimeFormatType.SHORT_FORMAT))


def getShortDateTimeFormat(value):
    return (u'{0:>s} {1:>s}').format(wulf.getDateFormat(value, wulf.DateFormatType.SHORT_FORMAT), wulf.getTimeFormat(value, wulf.TimeFormatType.SHORT_FORMAT))


def upper(value):
    return wulf.caseMap(value, wulf.CaseType.UPPERCASE)


def lower(value):
    return wulf.caseMap(value, wulf.CaseType.LOWERCASE)
