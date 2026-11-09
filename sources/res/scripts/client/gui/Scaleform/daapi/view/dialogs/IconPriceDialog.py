# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/IconPriceDialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconPriceDialog.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.IconPriceDialogMeta import IconPriceDialogMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n
from gui.shared.formatters import getItemPricesVO

class IconPriceDialog(IconPriceDialogMeta):

    def _populate(self):
        super(IconPriceDialog, self)._populate()
        self.as_setPriceLabelS(i18n.makeString(DIALOGS.REMOVECONFIRMATIONNOTREMOVABLEMONEY_MESSAGEPRICE))
        itemPrice = self._meta.getMessagePrice()
        pricesVO = getItemPricesVO(itemPrice)
        self.as_setMessagePriceS({'itemPrices': pricesVO, 'actionPrice': (self._meta.getAction())})
