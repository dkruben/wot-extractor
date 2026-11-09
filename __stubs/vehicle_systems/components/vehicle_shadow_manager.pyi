# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicle_shadow_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from cgf_script.registration import registerComponent as registerComponent

# decorador original: @registerComponent
class VehicleShadowManager(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    __compoundModel: Any
    __playerTargetChangeEvent: Any
    __cameraChangeModeEvent: Any
    __prevCameraMode: Any
    def __init__(self, compound=None, playerTargetChangeEvent=None, cameraChangeModeEvent=None):
        ...
    def changePlayerTarget(self, isStatic):
        ...
    def changeCameraMode(self, cameraMode, currentVehicleId=None):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def updatePlayerTarget(self, compoundModel):
        ...
    def registerCompoundModel(self, compoundModel):
        ...
    def unregisterCompoundModel(self, compoundModel):
        ...
    def reattachCompoundModel(self, vehicle, oldCompoundModel, newCompoundModel):
        ...

class VehicleShadowSystem(CGF.System):
    ManagerActivated: Any
    ManagerDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def __activateManager(self, manager):
        ...
    def __deactivateManager(self, manager):
        ...
