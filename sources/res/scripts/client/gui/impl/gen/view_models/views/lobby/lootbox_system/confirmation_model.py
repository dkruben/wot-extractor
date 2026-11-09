# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/confirmation_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/confirmation_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__ = ('confirm', 'cancel')

    def __init__(self, properties=2, commands=2):
        super(ConfirmationModel, self).__init__(properties=properties, commands=commands)

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getEventName(self):
        return self._getString(1)

    def setEventName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(ConfirmationModel, self)._initialize()
        self._addViewModelProperty('price', PriceItemModel())
        self._addStringProperty('eventName', '')
        self.confirm = self._addCommand('confirm')
        self.cancel = self._addCommand('cancel')
