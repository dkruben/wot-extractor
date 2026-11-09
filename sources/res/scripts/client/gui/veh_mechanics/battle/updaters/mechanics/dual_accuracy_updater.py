# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/dual_accuracy_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/mechanics/dual_accuracy_updater.py
from __future__ import absolute_import
import typing
from events_handler import eventHandler
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
if typing.TYPE_CHECKING:
    from DualAccuracy import DualAccuracy

class IDualAccuracyView(object):

    def setDualAccuracyState(self, isActive):
        raise NotImplementedError


class DualAccuracyUpdater(VehicleMechanicUpdater):

    def __init__(self, view):
        super(DualAccuracyUpdater, self).__init__(VehicleMechanicKeys.DUAL_ACCURACY, view)
        self.__dualAccuracyComponent = None
        return

    @eventHandler
    def onMechanicComponentCatching(self, component):
        self.__dualAccuracyComponent = component
        component.onSetDualAccState += self.__onSetDualAccState
        self.__onSetDualAccState(component.isActive())

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        component.onSetDualAccState -= self.__onSetDualAccState
        self.__dualAccuracyComponent = None
        return

    def destroy(self):
        self.__dualAccuracyComponent = None
        super(DualAccuracyUpdater, self).destroy()
        return

    def __onSetDualAccState(self, isActive):
        self.view.setDualAccuracyState(isActive)
