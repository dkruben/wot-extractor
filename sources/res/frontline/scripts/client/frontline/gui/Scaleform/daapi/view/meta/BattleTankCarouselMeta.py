# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/BattleTankCarouselMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/BattleTankCarouselMeta.py
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import CarouselEnvironment

class BattleTankCarouselMeta(CarouselEnvironment):

    def setFilter(self, id):
        self._printOverrideError('setFilter')

    def resetPlaylistAndFilters(self):
        self._printOverrideError('resetPlaylistAndFilters')

    def as_useExtendedCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_useExtendedCarousel(value)

    def as_scrollToSlotS(self, slotIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToSlot(slotIdx)
