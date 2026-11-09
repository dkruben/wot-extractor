# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/optional_devices_assistant_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset import OptionalDevicesAssistantPreset as OptionalDevicesAssistantPreset
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset_model_type import OptionalDevicesAssistantPresetModelType as OptionalDevicesAssistantPresetModelType

class OptionalDevicesAssistantItemType(Enum):
    STEREOSCOPE = 'stereoscope'
    TURBOCHARGER = 'turbocharger'
    ENHANCEDAIMDRIVES = 'enhancedAimDrives'
    COMMANDERSVIEW = 'commandersView'
    GROUSERS = 'grousers'
    ADDITINVISIBILITYDEVICE = 'additionalInvisibilityDevice'
    RADIOCOMMUNICATION = 'improvedRadioCommunication'
    ANTIFRAGMENTATIONLINING = 'antifragmentationLining'
    CAMOUFLAGENET = 'camouflageNet'
    ROTATIONMECHANISM = 'improvedRotationMechanism'
    VENTILATION = 'improvedVentilation'
    HEALTHRESERVE = 'extraHealthReserve'
    IMPROVEDSIGHTS = 'improvedSights'
    RAMMER = 'tankRammer'
    COATEDOPTICS = 'coatedOptics'
    AIMINGSTABILIZER = 'aimingStabilizer'
    IMPROVEDCONFIGURATION = 'improvedConfiguration'
    MODERNIZEDEXTRAHEALTHRESERVEANTIFRAGMENTATIONLINING = 'modernizedExtraHealthReserveAntifragmentationLining'
    MODERNIZEDTURBOCHARGERROTATIONMECHANISM = 'modernizedTurbochargerRotationMechanism'
    MODERNIZEDAIMDRIVESAIMINGSTABILIZER = 'modernizedAimDrivesAimingStabilizer'
    MODERNIZEDIMPROVEDSIGHTSENHANCEDAIMDRIVES = 'modernizedImprovedSightsEnhancedAimDrives'
    EMPTY = ''

class OptionalDevicesAssistantStateEnum(Enum):
    VISIBLE = 'visible'
    HIDDEN = 'hidden'
    NOTSUITABLEVEHICLE = 'notSuitableVehicle'
    NODATAATALL = 'noDataAtAll'

class OptionalDevicesAssistantModel(ViewModel):
    __slots__: tuple
    onPresetSelected: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def selectedPreset(self):
        ...
    @staticmethod
    def getSelectedPresetType():
        ...
    def getOptionalDevicesAssistantPresets(self):
        ...
    def setOptionalDevicesAssistantPresets(self, value):
        ...
    @staticmethod
    def getOptionalDevicesAssistantPresetsType():
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
