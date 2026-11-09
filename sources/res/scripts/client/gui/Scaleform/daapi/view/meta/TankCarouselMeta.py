# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.py
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import CarouselEnvironment

class TankCarouselMeta(CarouselEnvironment):

    def restoreTank(self):
        self._printOverrideError('restoreTank')

    def buyTank(self):
        self._printOverrideError('buyTank')

    def buySlot(self):
        self._printOverrideError('buySlot')

    def buyRentPromotion(self, intCD):
        self._printOverrideError('buyRentPromotion')

    def selectTelecomRentalVehicle(self, intCD):
        self._printOverrideError('selectTelecomRentalVehicle')

    def getCarouselAlias(self):
        self._printOverrideError('getCarouselAlias')

    def setFilter(self, id):
        self._printOverrideError('setFilter')

    def as_rowCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_rowCount(value)

    def as_setSmallDoubleCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSmallDoubleCarousel(value)

    def as_useExtendedCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_useExtendedCarousel(value)

    def as_scrollToSlotS(self, slotIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToSlot(slotIdx)
