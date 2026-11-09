# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/power_mode_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import bisect as bisect
import CGF as CGF
from GenericComponents import Sequence as Sequence
from constants import IS_CLIENT as IS_CLIENT
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from Vehicular import VehicleAudition as VehicleAudition
from vehicle_systems.tankStructure import TankSoundObjectsIndexes as TankSoundObjectsIndexes

class PowerModeController(object):
    ...

# decorador original: @registerComponent
class PowerModeRTPCComponent(object):
    category = 'Sound'
    editorTitle = 'PowerMode RTPC'
    domain = CGF.Domain.Client
    RTPCName: Any
    powerModeControllerGO: Any
    vehicleAuditionGO: Any
    progress: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class PowerModeActiveProgressLayers(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Power Mode Active Progress Layers'
    domain = CGF.Domain.Client
    points: Any
    transitionTime: Any
    layerNamePattern: Any
    powerModeControllerGO: Any
    requestedLayerName: Any
    progress: Any
    def __init__(self):
        ...

class PowerModeMechanicSystem(CGF.System):
    PowerModeProgressActivated: Any
    PowerModeProgressDectivated: Any
    PowerModeProgressIterate: Any
    PowerModeRTPCActivated: Any
    PowerModeRTPCDeactivated: Any
    PowerModeRTPCIterate: Any
    PowerModeControllerAccess: Any
    VehicleAuditionAccess: Any
    Reactions: Any
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    @classmethod
    def __getPowerModeActiveProgress(cls, powerModeControllerGO, powerModeAccess):
        ...
    @classmethod
    def __setEnginePowerMode(cls, powerModeRTPCComponent, powerModeAccess, auditionAccess):
        ...
    @classmethod
    def __requestActiveProgressLayer(cls, powerModeLayers, powerModeAccess, sequence, isInstantly=False):
        ...
