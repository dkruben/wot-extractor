# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/vehicle_title_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/widgets/vehicle_title_view.py
from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import VehicleTypes

class VehicleTitlePresenter(ViewComponent[VehicleTitleViewModel]):

    def __init__(self):
        super(VehicleTitlePresenter, self).__init__(R.aliases.halloween.shared.VehicleTitle(), VehicleTitleViewModel)

    def _onLoading(self, *args, **kwargs):
        super(VehicleTitlePresenter, self)._onLoading(*args, **kwargs)
        self._fillVehicle()

    @property
    def viewModel(self):
        return super(VehicleTitlePresenter, self).getViewModel()

    def _getEvents(self):
        return [
         (
          g_currentVehicle.onChanged, self.__onCurrentVehicleChanged)]

    def _fillVehicle(self):
        vehicle = g_currentVehicle.item
        if vehicle is not None:
            with self.viewModel.transaction() as tx:
                tx.setName(vehicle.userName)
                tx.setLevel(vehicle.level)
                tx.setIsPremium(vehicle.isPremium)
                tx.setVehicleType(VehicleTypes(vehicle.type) if vehicle.type != '' else VehicleTypes.NONE)
        return

    def __onCurrentVehicleChanged(self):
        if g_currentVehicle.item is None:
            return
        else:
            self._fillVehicle()
            return
