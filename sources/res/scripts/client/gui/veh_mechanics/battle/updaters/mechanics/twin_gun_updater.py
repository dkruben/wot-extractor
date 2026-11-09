# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/twin_gun_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/mechanics/twin_gun_updater.py
from __future__ import absolute_import
import typing
from events_handler import eventHandler
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
if typing.TYPE_CHECKING:
    from TwinGunController import TwinGunController

class ITwinGunView(object):

    def setDoubleBarrelMode(self, isActive):
        raise NotImplementedError


class TwinGunUpdater(VehicleMechanicUpdater):

    def __init__(self, view):
        super(TwinGunUpdater, self).__init__(VehicleMechanicKeys.TWIN_GUN, view)
        self.__twinGunComponent = None
        return

    @eventHandler
    def onMechanicComponentCatching(self, component):
        self.__twinGunComponent = component
        component.shootingEvents.onActiveGunsUpdate += self.__onActiveGunsUpdate
        self.__onActiveGunsUpdate(component.getActiveGunIndexes())

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        component.shootingEvents.onActiveGunsUpdate -= self.__onActiveGunsUpdate
        self.__twinGunComponent = None
        return

    def destroy(self):
        self.__twinGunComponent = None
        super(TwinGunUpdater, self).destroy()
        return

    def __onActiveGunsUpdate(self, _):
        self.view.setDoubleBarrelMode(self.__twinGunComponent.isDoubleBarrelMode())
