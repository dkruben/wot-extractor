# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/single_price_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/single_price_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel

class SinglePriceViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SinglePriceViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def cost(self):
        return self._getViewModel(0)

    @staticmethod
    def getCostType():
        return CurrencyViewModel

    @property
    def tooltip(self):
        return self._getViewModel(1)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getText(self):
        return self._getString(2)

    def setText(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(SinglePriceViewModel, self)._initialize()
        self._addViewModelProperty('cost', CurrencyViewModel())
        self._addViewModelProperty('tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty('text', '')
