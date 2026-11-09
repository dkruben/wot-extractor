# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/promo_window_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/promo_window_view_model.py
from frameworks.wulf import ViewModel

class PromoWindowViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(PromoWindowViewModel, self).__init__(properties=properties, commands=commands)

    def getStartDate(self):
        return self._getNumber(0)

    def setStartDate(self, value):
        self._setNumber(0, value)

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)

    def getRegularArtefactsLength(self):
        return self._getNumber(2)

    def setRegularArtefactsLength(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(PromoWindowViewModel, self)._initialize()
        self._addNumberProperty('startDate', 0)
        self._addNumberProperty('endDate', 0)
        self._addNumberProperty('regularArtefactsLength', 0)
        self.onClose = self._addCommand('onClose')
