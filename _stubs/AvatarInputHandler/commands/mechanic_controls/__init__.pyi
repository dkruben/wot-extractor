# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from AvatarInputHandler.commands.mechanic_controls.auto_shoot_gun_control import createAutoShootGunControl as createAutoShootGunControl
from AvatarInputHandler.commands.mechanic_controls.nitro_control import createNitroActivationControl as createNitroActivationControl
from AvatarInputHandler.commands.mechanic_controls.sight_pointer_control import createSightPointerActivationControl as createSightPointerActivationControl
from AvatarInputHandler.commands.mechanic_controls.simple_activation_control import createSimpleActivationControl as createSimpleActivationControl
from AvatarInputHandler.commands.mechanic_controls.stance_dance_control import createStanceDanceControl as createStanceDanceControl
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanics as getVehicleDescrMechanics
from items.vehicles import VehicleDescriptor as VehicleDescriptor
VEHICLE_MECHANIC_CONTROLS: dict

def createMechanicControls(vehicleDescriptor):
    ...
