# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/ls_carousel_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/ls_carousel_tooltip_view.py
from __future__ import absolute_import
import logging
from gui.impl.gen import R
from gui.impl.lobby.tooltips.carousel_vehicle_tooltip import CarouselVehicleTooltipView
from last_stand.gui.impl.lobby.ls_helpers import getLSVehicleStatus
_logger = logging.getLogger(__name__)

class LSVehicleCarouselTooltipView(CarouselVehicleTooltipView):
    LAYOUT_ID = R.views.last_stand.mono.lobby.tooltips.vehicle_tooltip()

    def _getVehicleStatus(self, vehicle):
        return getLSVehicleStatus(vehicle)
