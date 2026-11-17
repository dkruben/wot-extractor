# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/insignia_stickers_receiver_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GenericComponents as GenericComponents
import GpuDecals as GpuDecals
import Math as Math
from VehicleStickers import Insignia as Insignia
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_EDITOR as IS_EDITOR
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_systems.vehicle_composition import findParentVehicleAppearance as findParentVehicleAppearance, VehicleSlots as VehicleSlots

# decorador original: @registerComponent
class InsigniaStickersReceiverComponent(object):
    category = 'Render'
    editorTitle = 'Insignia Stickers Receiver Component'
    domain = CGF.Domain.ClientEditor
    vehiclePart: Any

class InsigniaStickersReceiverSystem(CGF.System):
    InsigniaAcitvated: Any
    InsigniaIterate: Any
    TransformAccess: Any
    hangarSpace: Any
    Reactions: Any
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    def onDecalsUpdated(self):
        ...
    def attach(self, gameobject, vehicleStickersReceiver, gpuDecalsReceiver, dynamicModelComponent, transformComponent, transformAccess):
        ...
    def vehicleChanged(self):
        ...
