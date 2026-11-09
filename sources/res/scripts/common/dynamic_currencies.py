# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dynamic_currencies.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dynamic_currencies.py
from __future__ import absolute_import
from hashlib import md5
from typing import Dict

class DynamicCurrenciesData:

    def __init__(self):
        self.__currencies = {}
        self.__loaded = False

    def getData(self):
        return self.__currencies

    def setData(self, data):
        self.__currencies = data
        self.__loaded = True

    def replaceData(self, data):
        self.__currencies.update(data)

    @property
    def loaded(self):
        return self.__loaded

    def isCurrencyCodeCorrect(self, currencyCode):
        return not self.__loaded or currencyCode in self.__currencies


def getCurrencyCD(currencyCode):
    cd_hex = md5(currencyCode).hexdigest()[:7]
    return int(cd_hex, 16)


g_dynamicCurrenciesData = DynamicCurrenciesData()
