# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_record_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_record_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.currency_value_model import CurrencyValueModel

class CurrencyRecordModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CurrencyRecordModel, self).__init__(properties=properties, commands=commands)

    @property
    def firstValue(self):
        return self._getViewModel(0)

    @staticmethod
    def getFirstValueType():
        return CurrencyValueModel

    @property
    def secondValue(self):
        return self._getViewModel(1)

    @staticmethod
    def getSecondValueType():
        return CurrencyValueModel

    def getLabel(self):
        return self._getResource(2)

    def setLabel(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(CurrencyRecordModel, self)._initialize()
        self._addViewModelProperty('firstValue', CurrencyValueModel())
        self._addViewModelProperty('secondValue', CurrencyValueModel())
        self._addResourceProperty('label', R.invalid())
