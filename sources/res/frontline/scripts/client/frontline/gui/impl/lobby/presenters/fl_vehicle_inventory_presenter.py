# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/fl_vehicle_inventory_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/presenters/fl_vehicle_inventory_presenter.py
from __future__ import absolute_import
from frontline.gui.impl.lobby.tooltips.carousel_vehicle_tooltip import FLCarouselVehicleTooltipView
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter
from gui.impl.gen import R

class FLVehicleInventoryPresenter(VehicleInventoryPresenter):

    def _getIsBpEntityValid(self):
        return False

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.hangar.vehicle_tooltip():
            return FLCarouselVehicleTooltipView(event.getArgument('inventoryId'))
        return super(FLVehicleInventoryPresenter, self).createToolTipContent(event=event, contentID=contentID)
