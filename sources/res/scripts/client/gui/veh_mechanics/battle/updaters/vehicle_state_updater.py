# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/vehicle_state_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/vehicle_state_updater.py
from __future__ import absolute_import
import logging, typing
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicle_state_ctrl import VehicleStateController
_logger = logging.getLogger(__name__)

class VehicleStateUpdater(ViewUpdater):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def initialize(self):
        super(VehicleStateUpdater, self).initialize()
        vehicleStateCtrl = self.__sessionProvider.shared.vehicleState
        if vehicleStateCtrl is None:
            _logger.error('No VehicleStateController found.')
            return
        else:
            vehicleStateCtrl.onVehicleStateUpdated += self.view.onVehicleStateUpdated
            return

    def finalize(self):
        vehicleStateCtrl = self.__sessionProvider.shared.vehicleState
        if vehicleStateCtrl is not None:
            vehicleStateCtrl.onVehicleStateUpdated -= self.view.onVehicleStateUpdated
        super(VehicleStateUpdater, self).finalize()
        return
