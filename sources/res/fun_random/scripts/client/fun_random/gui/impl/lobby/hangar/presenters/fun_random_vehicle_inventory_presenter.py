# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_vehicle_inventory_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_vehicle_inventory_presenter.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.impl.gen import R
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter
from gui.impl.lobby.tooltips.carousel_vehicle_tooltip import getUnsuitable2queueTooltip

class FunRandomVehicleInventoryPresenter(VehicleInventoryPresenter, FunAssetPacksMixin, FunSubModesWatcher):

    def createToolTip(self, event):
        if event.contentID == R.views.mono.hangar.vehicle_tooltip():
            desiredSubMode = self.getDesiredSubMode()
            if desiredSubMode is not None:
                vehicle = self._itemsCache.items.getVehicle(event.getArgument('inventoryId'))
                validationResult = desiredSubMode.isSuitableVehicle(vehicle)
                if validationResult is not None:
                    resPath = R.strings.fun_random.funRandomCarousel.lockedTooltip
                    return getUnsuitable2queueTooltip(self.getParentWindow(), event, validationResult, resPath, modeName=self.getModeUserName())
        return super(FunRandomVehicleInventoryPresenter, self).createToolTip(event)

    @hasDesiredSubMode()
    def _autoSelectVehicle(self):
        self._funRandomCtrl.hiddenVehicles.updateCurrentVehicle(self.getDesiredSubMode())
