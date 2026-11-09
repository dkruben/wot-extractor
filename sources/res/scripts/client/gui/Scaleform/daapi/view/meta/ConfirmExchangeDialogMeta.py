# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ConfirmExchangeDialogMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmExchangeDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmExchangeDialogMeta(AbstractWindowView):

    def exchange(self, goldValue):
        self._printOverrideError('exchange')

    def onSelectedAmountChanged(self, goldValue, needItemsValue):
        self._printOverrideError('onSelectedAmountChanged')

    def openDiscountInfoPage(self):
        self._printOverrideError('openDiscountInfoPage')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)

    def as_setExchangeValuesS(self, goldValue, needItemsValue, discountsAmountApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_setExchangeValues(goldValue, needItemsValue, discountsAmountApplied)
