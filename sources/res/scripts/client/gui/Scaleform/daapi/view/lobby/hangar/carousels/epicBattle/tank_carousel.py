# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/tank_carousel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/tank_carousel.py
from __future__ import absolute_import
from gui.filters.epic_battle_carousel_filter import EpicBattleCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.epicBattle.carousel_data_provider import EpicBattleCarouselDataProvider
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class EpicBattleTankCarousel(TankCarousel):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    _DISABLED_FILTERS = [
     'bonus']

    def __init__(self):
        super(EpicBattleTankCarousel, self).__init__()
        self._carouselDPCls = EpicBattleCarouselDataProvider
        self._carouselFilterCls = EpicBattleCarouselFilter

    def _populate(self):
        super(EpicBattleTankCarousel, self)._populate()
        self.as_useExtendedCarouselS(self.__epicController.isUnlockVehiclesInBattleEnabled())
        indexToScroll = self._carouselDP.getIndexToScroll()
        if indexToScroll >= 0:
            self.as_scrollToSlotS(indexToScroll)

    def _getInitialFilterVO(self, contexts):
        filtersVO = super(EpicBattleTankCarousel, self)._getInitialFilterVO(contexts)
        filtersVO['isFrontline'] = True
        for entry in filtersVO.get('hotFilters', []):
            if entry['id'] in self._DISABLED_FILTERS:
                entry['enabled'] = False
                entry['selected'] = False

        return filtersVO
