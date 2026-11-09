# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/select_vehicle/filter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/select_vehicle/filter.py
from __future__ import absolute_import
from account_helpers.AccountSettings import SELECT_VEHICLES_CAROUSEL_FILTER_1
from gui.filters.carousel_filter import BasicCriteriesGroup, CriteriesGroup, SessionCarouselFilter

class SelectVehiclesCriteriaGroup(BasicCriteriesGroup):

    def update(self, filters):
        CriteriesGroup.update(self, filters)
        self._setNationsCriteria(filters)
        self._setClassesCriteria(filters)
        self._setLevelsCriteria(filters)
        self._setEliteAndPremiumCriteria(filters)
        self._setFavoriteVehicleCriteria(filters)
        self._setVehicleNameCriteria(filters)


class SelectVehiclesCarouselFilter(SessionCarouselFilter):

    def __init__(self):
        super(SelectVehiclesCarouselFilter, self).__init__()
        self._clientSections = (SELECT_VEHICLES_CAROUSEL_FILTER_1,)
        self._criteriesGroups = (SelectVehiclesCriteriaGroup(),)
