# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/financial_details_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/financial_details_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_group_model import CurrencyGroupModel

class FinancialDetailsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FinancialDetailsModel, self).__init__(properties=properties, commands=commands)

    @property
    def earned(self):
        return self._getViewModel(0)

    @staticmethod
    def getEarnedType():
        return CurrencyGroupModel

    @property
    def expenses(self):
        return self._getViewModel(1)

    @staticmethod
    def getExpensesType():
        return CurrencyGroupModel

    @property
    def total(self):
        return self._getViewModel(2)

    @staticmethod
    def getTotalType():
        return CurrencyGroupModel

    @property
    def additional(self):
        return self._getViewModel(3)

    @staticmethod
    def getAdditionalType():
        return CurrencyGroupModel

    def _initialize(self):
        super(FinancialDetailsModel, self)._initialize()
        self._addViewModelProperty('earned', CurrencyGroupModel())
        self._addViewModelProperty('expenses', CurrencyGroupModel())
        self._addViewModelProperty('total', CurrencyGroupModel())
        self._addViewModelProperty('additional', CurrencyGroupModel())
