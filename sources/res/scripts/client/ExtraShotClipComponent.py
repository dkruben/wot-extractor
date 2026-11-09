# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ExtraShotClipComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ExtraShotClipComponent.py
from __future__ import absolute_import
from constants import ExtraShotClipStates
from events_handler import eventHandler
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState, AmmoShootPossibility
from gui.shared.utils.decorators import ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey, VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent

class ExtraShotAmmoState(DefaultComponentAmmoState):

    def __init__(self, reloadState):
        super(ExtraShotAmmoState, self).__init__()
        self.__reloadState = reloadState

    @property
    def extraReloadState(self):
        return self.__reloadState

    def isReloadAfterShot(self, timeLeft, baseTime):
        if self.__reloadState & ExtraShotClipStates.EXTRA_FULL_RELOAD:
            return self.__reloadState & ExtraShotClipStates.FULL_RELOAD_WITH_EXTRA_TIME
        return timeLeft == baseTime

    def getShootPossibility(self, currentShells):
        isShootPossible = currentShells[1] == 1 and bool(self.__reloadState & ExtraShotClipStates.EXTRA_FULL_RELOAD)
        if isShootPossible:
            return AmmoShootPossibility.ALLOWED
        return AmmoShootPossibility.NOT_DEFINED


@ReprInjector.withParent()
class ExtraShotClipComponent(VehicleDynamicComponent, IGunMechanicComponent):

    def __init__(self):
        super(ExtraShotClipComponent, self).__init__()
        self._initComponent()

    @property
    def vehicleMechanicKey(self):
        return VehicleMechanicKeys.EXTRA_SHOT_CLIP

    @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ammoStates[self.vehicleMechanicKey.uniqueName] = ExtraShotAmmoState(self.reloadState)
