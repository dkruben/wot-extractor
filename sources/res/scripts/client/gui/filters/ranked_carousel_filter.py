# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/filters/ranked_carousel_filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/filters/ranked_carousel_filter.py
import logging
from account_helpers.AccountSettings import RANKED_CAROUSEL_FILTER_1, RANKED_CAROUSEL_FILTER_2, RANKED_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, RANKED_CAROUSEL_FILTER_3
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter, BattlePassCriteriesGroup
from gui.filters.carousel_filter import EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController
_logger = logging.getLogger(__name__)

class RankedCarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(RankedCarouselFilter, self).__init__()
        self._serverSections = (RANKED_CAROUSEL_FILTER_1, RANKED_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1,
         RANKED_CAROUSEL_FILTER_3)
        self._clientSections = (RANKED_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)
        self._criteriesGroups = (EventCriteriesGroup(), RankedCriteriesGroup())


class RankedCriteriesGroup(BattlePassCriteriesGroup):
    __rankedBattlesController = dependency.descriptor(IRankedBattlesController)

    def update(self, filters):
        super(RankedCriteriesGroup, self).update(filters)
        if filters.get('ranked'):
            self._criteria |= REQ_CRITERIA.CUSTOM(self._rankedCriteria)

    @classmethod
    def _rankedCriteria(cls, vehicle):
        return cls.__rankedBattlesController.isSuitableVehicle(vehicle) is None
