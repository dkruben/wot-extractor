# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/gun_mechanics.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/gun_mechanics.py
from __future__ import absolute_import
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from items.vehicle_mechanics_types import VehicleMechanicKeys

class GunMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        return [
         (
          guiItem.isAutoShoot(vehDescr), VehicleMechanicKeys.AUTO_SHOOT_GUN),
         (
          guiItem.isDualGun(vehDescr), VehicleMechanicKeys.DUAL_GUN),
         (
          guiItem.hasMechanic(VehicleMechanicKeys.DUAL_ACCURACY, vehDescr), VehicleMechanicKeys.DUAL_ACCURACY),
         (
          guiItem.isTwinGun(vehDescr), VehicleMechanicKeys.TWIN_GUN),
         (
          guiItem.isClipGun(vehDescr), VehicleMechanicKeys.MAGAZINE_GUN),
         (
          guiItem.isLowChargeShotGun(vehDescr), VehicleMechanicKeys.LOW_CHARGE_SHOT),
         (
          guiItem.isAutoReloadableWithBoost(vehDescr), VehicleMechanicKeys.AUTO_LOADER_GUN_BOOST),
         (
          guiItem.isAutoReloadable(vehDescr) and not guiItem.isAutoReloadableWithBoost(vehDescr),
          VehicleMechanicKeys.AUTO_LOADER_GUN),
         (
          guiItem.isDamageMutable(), VehicleMechanicKeys.DAMAGE_MUTABLE),
         (
          any(shell.descriptor.hasStun for shell in guiItem.defaultAmmo), VehicleMechanicKeys.STUN)]

    @classmethod
    def _getMechanicsParams(cls, guiItem, vehDescr):
        return guiItem.getDescriptor(vehDescr).mechanicsParams
