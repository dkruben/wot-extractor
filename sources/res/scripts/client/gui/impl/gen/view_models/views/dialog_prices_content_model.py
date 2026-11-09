# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialog_prices_content_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialog_prices_content_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.value_price import ValuePrice

class DialogPricesContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DialogPricesContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def valueMain(self):
        return self._getViewModel(0)

    @staticmethod
    def getValueMainType():
        return ValuePrice

    @property
    def valueAdditional(self):
        return self._getViewModel(1)

    @staticmethod
    def getValueAdditionalType():
        return ValuePrice

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)

    def getHasAdditionalCost(self):
        return self._getBool(3)

    def setHasAdditionalCost(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(DialogPricesContentModel, self)._initialize()
        self._addViewModelProperty('valueMain', ValuePrice())
        self._addViewModelProperty('valueAdditional', ValuePrice())
        self._addNumberProperty('tooltipId', 0)
        self._addBoolProperty('hasAdditionalCost', False)
