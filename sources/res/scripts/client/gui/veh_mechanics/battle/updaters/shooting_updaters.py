# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/shooting_updaters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/shooting_updaters.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.vehicle_passenger import hasVehiclePassengerCtrl, VehiclePassengerInfoWatcher
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from items.components.gun_installation_components import GunInstallationSlot

class IShootingReactionsView(object):

    def onDiscreteShotsDone(self, gunInstallationSlot, isCurrentVehicle):
        raise NotImplementedError


class ShootingReactionsUpdater(ViewUpdater, VehiclePassengerInfoWatcher):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def initialize(self):
        super(ShootingReactionsUpdater, self).initialize()
        feedbackCtrl = self.__sessionProvider.shared.feedback
        if feedbackCtrl is not None:
            feedbackCtrl.onDiscreteShotsDone += self.__onDiscreteShotsDone
        return

    def finalize(self):
        feedbackCtrl = self.__sessionProvider.shared.feedback
        if feedbackCtrl is not None:
            feedbackCtrl.onDiscreteShotsDone -= self.__onDiscreteShotsDone
        super(ShootingReactionsUpdater, self).finalize()
        return

    @hasVehiclePassengerCtrl()
    def __onDiscreteShotsDone(self, entityID, gunInstallationSlot, passengerCtrl=None):
        self.view.onDiscreteShotsDone(gunInstallationSlot, entityID == passengerCtrl.currentVehicleID)
