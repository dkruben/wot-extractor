# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/filters/mapbox_carousel_filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/filters/mapbox_carousel_filter.py
from account_helpers.AccountSettings import MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, MAPBOX_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, MAPBOX_CAROUSEL_FILTER_3
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter

class MapboxCarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(MapboxCarouselFilter, self).__init__()
        self._serverSections = (MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1,
         MAPBOX_CAROUSEL_FILTER_3)
        self._clientSections = (MAPBOX_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)
