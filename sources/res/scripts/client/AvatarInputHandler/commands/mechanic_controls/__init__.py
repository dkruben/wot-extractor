# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/mechanic_controls/__init__.py
from __future__ import absolute_import
import typing
from AvatarInputHandler.commands.mechanic_controls.auto_shoot_gun_control import createAutoShootGunControl
from AvatarInputHandler.commands.mechanic_controls.nitro_control import createNitroActivationControl
from AvatarInputHandler.commands.mechanic_controls.sight_pointer_control import createSightPointerActivationControl
from AvatarInputHandler.commands.mechanic_controls.simple_activation_control import createSimpleActivationControl
from AvatarInputHandler.commands.mechanic_controls.stance_dance_control import createStanceDanceControl
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanics
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
VEHICLE_MECHANIC_CONTROLS = {(VehicleMechanicKeys.AUTO_SHOOT_GUN): createAutoShootGunControl, 
   (VehicleMechanicKeys.AUTORELOADER_SURGE): createSimpleActivationControl, 
   (VehicleMechanicKeys.CHARGE_SHOT): createSimpleActivationControl, 
   (VehicleMechanicKeys.COMBAT_THROTTLE): createSimpleActivationControl, 
   (VehicleMechanicKeys.CONCENTRATION_MODE): createSimpleActivationControl, 
   (VehicleMechanicKeys.PROPELLANT_GUN): createSimpleActivationControl, 
   (VehicleMechanicKeys.ROCKET_ACCELERATION): createSimpleActivationControl, 
   (VehicleMechanicKeys.RECHARGEABLE_NITRO): createNitroActivationControl, 
   (VehicleMechanicKeys.SIGHT_POINTER): createSightPointerActivationControl, 
   (VehicleMechanicKeys.STANCE_DANCE): createStanceDanceControl, 
   (VehicleMechanicKeys.STATIONARY_RELOAD): createSimpleActivationControl, 
   (VehicleMechanicKeys.SUPPORT_WEAPON): createSimpleActivationControl, 
   (VehicleMechanicKeys.TARGET_DESIGNATOR): createSimpleActivationControl}

def createMechanicControls(vehicleDescriptor):
    return tuple(VEHICLE_MECHANIC_CONTROLS[mechanic](mechanic) for mechanic in getVehicleDescrMechanics(vehicleDescriptor) if mechanic in VEHICLE_MECHANIC_CONTROLS)
