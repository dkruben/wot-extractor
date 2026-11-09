# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/vehicle_hub_characteristics_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/vehicle_hub_characteristics_presenter.py
from __future__ import absolute_import
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import VehicleParamsPresenter
from gui.impl.gen import R
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.items_parameters import params_helper

class VehicleHubCharacteristicsPresenter(VehicleParamsPresenter):

    def __init__(self, vehIntCD):
        super(VehicleHubCharacteristicsPresenter, self).__init__(vehIntCD, layoutID=R.aliases.common.none(), applyFormatting=False)

    def _getComparator(self):
        vehicle = self._getVehicle()
        return params_helper.tankSetupVehiclesComparator(vehicle, vehicle)

    def _isExtraParamEnabled(self):
        return True

    def _isAdditionalValueEnabled(self):
        return True

    def _getIsOpened(self, groupName):
        return True

    def _getParamTooltips(self):
        parentTooltips = super(VehicleHubCharacteristicsPresenter, self)._getParamTooltips()
        return parentTooltips | {TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_ADVANCED_PARAMETERS}
