# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/carousel_vehicle_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/tooltips/carousel_vehicle_tooltip.py
from __future__ import absolute_import
import typing
from gui.impl.lobby.tooltips.carousel_vehicle_tooltip import CarouselVehicleTooltipView
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class FLCarouselVehicleTooltipView(CarouselVehicleTooltipView):

    def _getDailyXPFactor(self, vehicle):
        return -1

    def _getBpProgression(self, vehicleIntCD):
        bpPoints, _ = self._battlePass.getVehicleProgression(vehicleIntCD)
        return (bpPoints, 0)

    def _getIsBpEntityValid(self):
        return False
