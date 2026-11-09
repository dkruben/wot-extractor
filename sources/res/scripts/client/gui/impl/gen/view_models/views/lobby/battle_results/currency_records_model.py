# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_records_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_records_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel

class CurrencyRecordsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CurrencyRecordsModel, self).__init__(properties=properties, commands=commands)

    def getEarned(self):
        return self._getArray(0)

    def setEarned(self, value):
        self._setArray(0, value)

    @staticmethod
    def getEarnedType():
        return CurrencyRecordsItemModel

    def getExpenses(self):
        return self._getArray(1)

    def setExpenses(self, value):
        self._setArray(1, value)

    @staticmethod
    def getExpensesType():
        return CurrencyRecordsItemModel

    def getTotal(self):
        return self._getArray(2)

    def setTotal(self, value):
        self._setArray(2, value)

    @staticmethod
    def getTotalType():
        return CurrencyRecordsItemModel

    def _initialize(self):
        super(CurrencyRecordsModel, self)._initialize()
        self._addArrayProperty('earned', Array())
        self._addArrayProperty('expenses', Array())
        self._addArrayProperty('total', Array())
