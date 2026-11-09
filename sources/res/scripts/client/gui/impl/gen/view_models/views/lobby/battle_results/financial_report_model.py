# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/financial_report_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/financial_report_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_model import CurrencyRecordsModel

class FinancialReportModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FinancialReportModel, self).__init__(properties=properties, commands=commands)

    @property
    def crystals(self):
        return self._getViewModel(0)

    @staticmethod
    def getCrystalsType():
        return CurrencyRecordsModel

    @property
    def xp(self):
        return self._getViewModel(1)

    @staticmethod
    def getXpType():
        return CurrencyRecordsModel

    @property
    def freeXp(self):
        return self._getViewModel(2)

    @staticmethod
    def getFreeXpType():
        return CurrencyRecordsModel

    @property
    def credits(self):
        return self._getViewModel(3)

    @staticmethod
    def getCreditsType():
        return CurrencyRecordsModel

    @property
    def gold(self):
        return self._getViewModel(4)

    @staticmethod
    def getGoldType():
        return CurrencyRecordsModel

    def _initialize(self):
        super(FinancialReportModel, self)._initialize()
        self._addViewModelProperty('crystals', CurrencyRecordsModel())
        self._addViewModelProperty('xp', CurrencyRecordsModel())
        self._addViewModelProperty('freeXp', CurrencyRecordsModel())
        self._addViewModelProperty('credits', CurrencyRecordsModel())
        self._addViewModelProperty('gold', CurrencyRecordsModel())
