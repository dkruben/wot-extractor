# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/mapbox/tank_carousel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/mapbox/tank_carousel.py
from __future__ import absolute_import
from constants import Configs
from gui.filters.mapbox_carousel_filter import MapboxCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.mapbox.carousel_data_provider import MapboxCarouselDataProvider
from helpers import server_settings

class MapboxTankCarousel(BattlePassTankCarousel):

    def __init__(self):
        super(MapboxTankCarousel, self).__init__()
        self._carouselDPCls = MapboxCarouselDataProvider
        self._carouselFilterCls = MapboxCarouselFilter

    def _onServerSettingChanged(self, diff, skipVehicles=False):
        super(MapboxTankCarousel, self)._onServerSettingChanged(diff, skipVehicles=self.__onServerSettingChanged(diff))

    @server_settings.serverSettingsChangeListener(Configs.MAPBOX_CONFIG.value)
    def __onServerSettingChanged(self, *_):
        self.updateVehicles()
