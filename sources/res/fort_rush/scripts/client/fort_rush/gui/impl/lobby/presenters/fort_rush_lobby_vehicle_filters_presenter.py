# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_lobby_vehicle_filters_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_lobby_vehicle_filters_presenter.py
from __future__ import absolute_import
from typing import List
from gui.filters.carousel_filter import FILTER_KEYS
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME
_VEHICLE_TYPES_ORDER = (
 VEHICLE_CLASS_NAME.LIGHT_TANK,
 VEHICLE_CLASS_NAME.MEDIUM_TANK,
 VEHICLE_CLASS_NAME.HEAVY_TANK,
 VEHICLE_CLASS_NAME.AT_SPG)

class FortRushLobbyVehicleFiltersPresenter(VehicleFiltersDataProvider):

    @classmethod
    def _getVehicleTypesFilter(cls):
        return _VEHICLE_TYPES_ORDER

    @classmethod
    def _getBaseSpecialSection(cls):
        return [
         FILTER_KEYS.EVENT,
         FILTER_KEYS.FAVORITE,
         FILTER_KEYS.RENTED,
         FILTER_KEYS.ELITE,
         FILTER_KEYS.PREMIUM,
         FILTER_KEYS.OWN_3D_STYLE,
         FILTER_KEYS.CAN_INSTALL_ATTACHMENTS]
