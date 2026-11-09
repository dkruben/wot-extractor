# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/carousels/carousel_filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/carousels/carousel_filter.py
from __future__ import absolute_import
from account_helpers.AccountSettings import COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2, COMP7_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, COMP7_CAROUSEL_FILTER_3
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter, BattlePassCriteriesGroup
from gui.filters.carousel_filter import EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7CarouselFilter(BattlePassCarouselFilter):

    def __init__(self):
        super(Comp7CarouselFilter, self).__init__()
        self._serverSections = (COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2, BATTLEPASS_CAROUSEL_FILTER_1,
         COMP7_CAROUSEL_FILTER_3)
        self._clientSections = (COMP7_CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1)
        self._criteriesGroups = (
         EventCriteriesGroup(), Comp7CriteriesGroup())


class Comp7CriteriesGroup(BattlePassCriteriesGroup):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def update(self, filters):
        super(Comp7CriteriesGroup, self).update(filters)
        if filters.get('comp7'):
            self._criteria |= REQ_CRITERIA.CUSTOM(self._comp7Criteria)

    @classmethod
    def _comp7Criteria(cls, vehicle):
        return cls.__comp7Controller.isSuitableVehicle(vehicle) is None
