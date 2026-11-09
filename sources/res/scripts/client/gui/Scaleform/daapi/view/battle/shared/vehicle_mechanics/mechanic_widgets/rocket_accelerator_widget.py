# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/rocket_accelerator_widget.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/rocket_accelerator_widget.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.meta.RocketAcceleratorIndicatorMeta import RocketAcceleratorIndicatorMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.rocket_accelerator_updater import IRocketAcceleratorView, RocketAcceleratorUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
if typing.TYPE_CHECKING:
    from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater

class RocketAcceleratorMechanicIndicator(RocketAcceleratorIndicatorMeta, IRocketAcceleratorView):

    def setCount(self, count):
        self.as_setCountS(count)

    def setProgress(self, progress):
        self.as_setProgressS(progress)

    def setState(self, state, isInstantly=False):
        self.as_setStateS(state, isInstantly=isInstantly)

    def setTime(self, time):
        self.as_setTimeS(time)

    def _getViewUpdaters(self):
        return [
         VehicleMechanicPassengerUpdater(VehicleMechanicKeys.ROCKET_ACCELERATION, self),
         RocketAcceleratorUpdater(self)]
