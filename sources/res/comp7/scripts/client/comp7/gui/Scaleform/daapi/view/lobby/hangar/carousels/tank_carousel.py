# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/carousels/tank_carousel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/carousels/tank_carousel.py
from __future__ import absolute_import
from comp7.gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_data_provider import Comp7CarouselDataProvider
from comp7.gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_filter import Comp7CarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel

class Comp7TankCarousel(BattlePassTankCarousel):

    def __init__(self):
        super(Comp7TankCarousel, self).__init__()
        self._carouselDPCls = Comp7CarouselDataProvider
        self._carouselFilterCls = Comp7CarouselFilter

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(Comp7TankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO['isComp7'] = True
        return filtersVO
