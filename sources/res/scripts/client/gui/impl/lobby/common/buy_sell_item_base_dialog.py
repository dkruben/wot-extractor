# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/buy_sell_item_base_dialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/buy_sell_item_base_dialog.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow, createTooltipData
from gui.impl.gen import R
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
if TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.common.buy_sell_items_dialog_model import BuySellItemsDialogModel

class DialogBuySellItemBaseView(FullScreenDialogView):

    def __init__(self, settings, typeCompDescr):
        super(DialogBuySellItemBaseView, self).__init__(settings)
        self._itemCD = typeCompDescr
        self._item = self._itemsCache.items.getItemByCD(self._itemCD)

    @property
    def viewModel(self):
        raise NotImplementedError

    @property
    def isBuying(self):
        raise NotImplementedError

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument('tooltipId')
            if tooltipId == TOOLTIPS_CONSTANTS.ACTION_PRICE:
                itemPrice = self._getItemPrice()
                args = (
                 ACTION_TOOLTIPS_TYPE.ITEM,
                 self._item.intCD,
                 list(itemPrice.price),
                 list(itemPrice.defPrice),
                 self.isBuying)
                window = BackportTooltipWindow(createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=args), self.getParentWindow())
                window.load()
                return window
        return super(DialogBuySellItemBaseView, self).createToolTip(event)

    def _setBaseParams(self, model):
        super(DialogBuySellItemBaseView, self)._setBaseParams(model)
        self._setItemPrices(model)
        model.setBackgroundImg(R.images.gui.maps.shop.artefacts.c_180x135.dyn(self._item.descriptor.icon[0])())

    def _getItemPrice(self):
        if self.isBuying:
            price = self._item.getBuyPrice(preferred=False)
        else:
            price = self._item.getSellPrice(preferred=False)
        return price

    def _setItemPrices(self, model):
        itemPrice = self._getItemPrice()
        currency = itemPrice.getCurrency(byWeight=True)
        model.setCurrencyType(currency)
        model.setItemPrice(itemPrice.price.getSignValue(currency))
        count = model.getItemCount()
        model.setItemTotalPrice(count * itemPrice.price.getSignValue(currency))
        model.setIsAlert(itemPrice.isActionPrice())

    def _finalize(self):
        super(DialogBuySellItemBaseView, self)._finalize()
        self._item = None
        return
