# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_carousel_filters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_carousel_filters.py
from __future__ import absolute_import
from gui.filters.carousel_filter import RoleCriteriesGroup
from gui.shared.utils.requesters.ItemsRequester import RequestCriteria, PredicateCondition
FL_RENT = RequestCriteria(PredicateCondition((lambda item: item.name.endswith('_FL'))))

class FLRentedCriteriaGroup(RoleCriteriesGroup):

    def update(self, filters):
        super(FLRentedCriteriaGroup, self).update(filters)
        if not filters['rented']:
            self._criteria |= ~FL_RENT

    @staticmethod
    def isApplicableFor(vehicle):
        return True
