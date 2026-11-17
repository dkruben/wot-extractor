# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/decal_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GpuDecals as GpuDecals
import GenericComponents as GenericComponents
from vehicle_systems.vehicle_composition import findParentVehicleAppearance as findParentVehicleAppearance
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes, TankPartNames as TankPartNames
from GenericComponents import DecalComponent as DecalComponent, SlotMarkerComponent as SlotMarkerComponent

class DecalComponentSystem(CGF.System):
    DecalActivated: Any
    DecalReceiverActivated: Any
    DecalReceiverWithSlotActivated: Any
    DecalReceiverDeactivated: Any
    DecalComponentAccess: Any
    ReceiverAccess: Any
    Reactions: Any
    def update(self):
        ...
    @staticmethod
    def __bindReceiver(decal, receiver, receiverAccess):
        ...
    @staticmethod
    def __unbindReceiver(decal):
        ...
    @staticmethod
    def __isReceiverBinded(decal):
        ...
