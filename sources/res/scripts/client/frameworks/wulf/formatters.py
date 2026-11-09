# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/formatters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/formatters.py
from __future__ import absolute_import
import typing
from .gui_constants import NumberFormatType, RealFormatType
from .gui_constants import TimeFormatType, DateFormatType
from .py_object_binder import PyObjectEntity

class Formatters(PyObjectEntity):

    @classmethod
    def create(cls, proxy):
        _formatters = Formatters()
        _formatters.bind(proxy)
        return _formatters

    def destroy(self):
        self.unbind()

    def getNumberFormat(self, value, formatType=NumberFormatType.INTEGRAL):
        return self.proxy.getNumberFormat(int(value), formatType)

    def getRealFormat(self, value, formatType=RealFormatType.FRACTIONAL, fractionLen=2):
        return self.proxy.getRealFormat(value, formatType, fractionLen)

    def getTimeFormat(self, value, formatType=TimeFormatType.SHORT_FORMAT):
        return self.proxy.getTimeFormat(value, formatType)

    def getDateFormat(self, value, formatType=DateFormatType.SHORT_FORMAT):
        return self.proxy.getDateFormat(value, formatType)

    def caseMap(self, value, caseType):
        return self.proxy.caseMap(value, caseType)
