# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/shake_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import BigWorld as BigWorld
import Math as Math
from aih_constants import ShakeReason as ShakeReason
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
from Vehicle import Vehicle as Vehicle

def shakePlayerDynamicCamera(vehicle, gunInstallationSlot, shakeReason=..., gunNodeName=..., gunFireNodeName='HP_gunFire'):
    ...
def shakeMultiGunPlayerDynamicCamera(vehicle, gunInstallationSlot, gunIndex, shakeReason=...):
    ...
def shakeMultiGunsPlayerDynamicCamera(vehicle, gunInstallationSlot, gunIndexes, shakeReason=...):
    ...
