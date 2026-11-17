# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/optional_devices_assistant_preset.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_item import OptionalDevicesAssistantItem as OptionalDevicesAssistantItem
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset_model_type import OptionalDevicesAssistantPresetModelType as OptionalDevicesAssistantPresetModelType

class OptionalDevicesAssistantTypeEnum(IntEnum):
    NODATA = 0
    NORMAL = 1
    LINKED = 2
    COMBINED = 3

class OptionalDevicesAssistantModeTypeEnum(Enum):
    UNKNOWN = 'unknown'
    RANDOM = 'random'
    COMP7 = 'comp7'

class OptionalDevicesAssistantPreset(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    @property
    def presetType(self):
        ...
    @staticmethod
    def getPresetTypeType():
        ...
    def getOptionalDevicesResultType(self):
        ...
    def setOptionalDevicesResultType(self, value):
        ...
    def getModeType(self):
        ...
    def setModeType(self, value):
        ...
    def getSourceVehicleCompDescr(self):
        ...
    def setSourceVehicleCompDescr(self, value):
        ...
    def getIsDataOutdated(self):
        ...
    def setIsDataOutdated(self, value):
        ...
    def getOptionalDevicesAssistantItems(self):
        ...
    def setOptionalDevicesAssistantItems(self, value):
        ...
    @staticmethod
    def getOptionalDevicesAssistantItemsType():
        ...
    def _initialize(self):
        ...
