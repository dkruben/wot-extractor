# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/hangar/presenters/comp7_core_vehicle_filters_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/impl/lobby/hangar/presenters/comp7_core_vehicle_filters_presenter.py
from __future__ import absolute_import
import typing
from gui.filters.carousel_filter import FILTER_KEYS
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider
if typing.TYPE_CHECKING:
    from typing import List

class Comp7CoreVehicleFiltersDataProvider(VehicleFiltersDataProvider):

    @classmethod
    def _getBaseSpecialSection(cls):
        specialSection = super(Comp7CoreVehicleFiltersDataProvider, cls)._getBaseSpecialSection()
        specialSection.append(FILTER_KEYS.EVENT)
        return specialSection
