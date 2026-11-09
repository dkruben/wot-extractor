# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/congrats/congrats_ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/congrats/congrats_ctx.py
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.RES_SHOP import RES_SHOP
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import getShopVehicleIconPath
from skeletons.gui.shared.congrats import ICongratsCtx

class CongratsCtx(ICongratsCtx):

    @property
    def background(self):
        return R.images.gui.maps.icons.store.shop_2_background_arsenal()

    @property
    def title(self):
        return R.strings.store.congratulationAnim.buyingLabel()

    @property
    def description(self):
        return ''

    @property
    def image(self):
        return self.imageAlt

    @property
    def imageAlt(self):
        return getShopVehicleIconPath(STORE_CONSTANTS.ICON_SIZE_LARGE, 'empty_tank')

    @property
    def confirmLabel(self):
        return R.strings.store.congratulationAnim.confirmLabel()

    @property
    def backLabel(self):
        return R.invalid()

    def onConfirm(self):
        pass

    def onBack(self):
        pass


class GUIItemCongratsCtx(CongratsCtx):

    def __init__(self, item):
        self._item = item


class StyleCongratsCtx(GUIItemCongratsCtx):

    @property
    def description(self):
        return backport.text(R.strings.store.congratulationAnim.descriptionLabel.style(), name=self._item.userName)

    @property
    def image(self):
        size = STORE_CONSTANTS.ICON_SIZE_LARGE
        if RES_SHOP.hasStyleIcon(size, self._item.id):
            return RES_SHOP.getStyleIcon(size, self._item.id)
        return self._item.icon
