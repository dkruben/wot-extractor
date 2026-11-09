# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/filter.py
from __future__ import absolute_import
from account_helpers.AccountSettings import ROYALE_CAROUSEL_FILTER_1, ROYALE_CAROUSEL_FILTER_2, ROYALE_CAROUSEL_FILTER_CLIENT_1
from gui.filters import carousel_filter

class RoyaleCarouselFilter(carousel_filter.CarouselFilter):

    def __init__(self):
        super(RoyaleCarouselFilter, self).__init__()
        self._serverSections = (ROYALE_CAROUSEL_FILTER_1, ROYALE_CAROUSEL_FILTER_2)
        self._clientSections = (ROYALE_CAROUSEL_FILTER_CLIENT_1,)

    def _setCriteriaGroups(self):
        self._criteriesGroups = (
         carousel_filter.EventCriteriesGroup(),
         carousel_filter.BasicCriteriesGroup())

    def _getFromServerStorage(self, defaultFilters):
        return defaultFilters
