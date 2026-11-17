# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicle_assembly_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from collections import namedtuple as namedtuple
import CGF as CGF
import GenericComponents as GenericComponents
import GpuDecals as GpuDecals
import Vehicular as Vehicular
import Compound as Compound
from cgf_components.client_worlds_helpers import ClientWorld as ClientWorld, getClientWorld as getClientWorld
from cgf_modules.variable_components import VariableStorageComponent as VariableStorageComponent
from constants import IS_UE_EDITOR as IS_UE_EDITOR
from vehicle_systems import vehicle_composition as veh_comp
from vehicle_systems.components import vehicle_variable_storage as vehicle_variable_storage
from vehicle_systems.tankStructure import TankPartNames as TankPartNames, TankRenderMode as TankRenderMode, ModelStates as ModelStates, TankNodeNames as TankNodeNames
from GenericComponents import SlotMarkerComponent as SlotMarkerComponent
from vehicle_appearance.common_tank_appearance import CommonTankAppearance as CommonTankAppearance
from gui.hangar_vehicle_appearance import HangarVehicleAppearance as HangarVehicleAppearance
from vehicle_systems.components.vehicle_variable_storage import VariableType as VariableType
TAppearance: Any
_logger: Any
_AssemblerData: Any

class Assembler(object):
    NodeFollowerAccess: Any
    AccessReactions: Any
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, *args):
        ...
    @staticmethod
    def _replaceWithNodeDriver(go, appearance, queue, nodeFollowerAccess):
        ...

class TurretGunRotationAssembler(Assembler):
    _SLOTS: tuple
    AccessReactions: tuple
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue, nodeFollowerAccess):
        ...
    def __getMatrixProvider(self, slotName, appearance):
        ...

class TurretJointRotationAssembler(Assembler):
    _SLOTS = TankNodeNames.TURRET_JOINT
    AccessReactions: Any
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue):
        ...
    def __getMatrixProvider(self, slotName, appearance):
        ...

class RecoilAssembler(Assembler):
    _SLOTS: tuple
    AccessReactions: tuple
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, _, queue, nodeFollowerAccess):
        ...
    def _createComponent(self, gameObject, appearance, queue, nodeFollowerAccess):
        ...

class MultiGunRecoilAssembler(RecoilAssembler):
    _SLOTS: tuple
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue, nodeFollowerAccess):
        ...

class SwingingAnimationManager(Assembler):
    LodCalculatorAccess: Any
    TransformAccess: Any
    AccessReactions: tuple
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue, lodCalculatorAccess, transformAccess, nodeFollowerAccess):
        ...
    def __assembleSwinging(self, gameObject, appearance, queue, lodCalculatorAccess, transformAccess, nodeFollowerAccess):
        ...
    def __createSwingingAnimator(self, queue, gameObject, transformAccess, vehicleDesc, basisMatrix, appearanceGo, lodLink=None):
        ...

class DecalsAssembler(Assembler):
    _SLOTS: tuple
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue):
        ...

class GunInfoAssembler(Assembler):
    _SLOTS: tuple
    VariableStorageAccess: Any
    AccessReactions: tuple
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue, varStorageAccess):
        ...
    @staticmethod
    def update(appearance, varName, value):
        ...
    @staticmethod
    def _isStorageRequired(typeDescriptor):
        ...

class CompositionReadinessNotifier(Assembler):
    def checkSlotMarker(self, slotMarker):
        ...
    def assemble(self, gameObject, slotMarker, queue):
        ...

class VehicleAssemblySystem(CGF.System):
    MarkerActivated: Any
    _assemblers: tuple
    _assemblerReactions: Any
    Reactions: Any
    __assemblers: Any
    def __init__(self):
        ...
    def update(self):
        ...

class HangarVehicleStateSwitcherSystem(CGF.System):
    SwitcherActivated: Any
    Reactions: Any
    def update(self):
        ...

def _isAlive(appearance):
    ...
