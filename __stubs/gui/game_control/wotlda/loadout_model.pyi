# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wotlda/loadout_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import List as List, Tuple as Tuple, Union as Union, Any as Any, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from dict2model import models as models, fields as fields, utils as utils
from dict2model.schemas import Schema as Schema, validate as validate
from gui.game_control.wotlda.constants import EQUIPMENT_ARCHETYPE_1 as EQUIPMENT_ARCHETYPE_1, EQUIPMENT_ARCHETYPE_2 as EQUIPMENT_ARCHETYPE_2, EQUIPMENT_ARCHETYPE_3 as EQUIPMENT_ARCHETYPE_3, ExpectedArchetypes as ExpectedArchetypes, OptDeviceAssistType as OptDeviceAssistType, LOADOUT_USAGE_PERCENTAGE as LOADOUT_USAGE_PERCENTAGE
from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout as VehicleLoadout, EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP as EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP
from dict2model.fields import Number as Number
_OptDevicePreset: _Any
_MODERNIZED_ARCHETYPES_TO_SIMPLE_DEVICES: dict
_SIMPLE_DEVICES_TO_MODERNIZED_ARCHETYPES: dict
baseOptDeviceLoadoutSchema: _Any
vehicleOptDeviceLoadoutsSchema: _Any

class VehicleIdField(fields.Integer):
    def _deserialize(self, incoming, **kwargs):
        ...

class PercentageField(fields.Float):
    def _deserialize(self, incoming, **kwargs):
        ...

class NullString(fields.String):
    def _deserialize(self, incoming, **kwargs):
        ...

class OneOfArchetypes(validate.OneOf):
    def __call__(self, incoming):
        ...

class EquipmentField(NullString):
    def __init__(self):
        ...

class EmptyLoadoutField(fields.UniCapList):
    def _convert(self, incoming, skipValidation, converter, **kwargs):
        ...

class PercentRange(validate.Range):
    def __init__(self):
        ...
    def __call__(self, incoming):
        ...

class BaseOptDeviceLoadoutModel(models.Model):
    __slots__: tuple
    linkedVehicleID: _Any
    equipmentArchetype1: _Any
    equipmentArchetype2: _Any
    equipmentArchetype3: _Any
    usagePercentage: _Any
    def __init__(self, vehicle_id, equipment_archetype_id_1, equipment_archetype_id_2, equipment_archetype_id_3, usage_percentage):
        ...
    def getDevices(self, getModernized=False):
        ...
    def _getDeviceTierArchetype(self, device):
        ...

# base nao representavel no stub: Schema[...]
class BaseOptDeviceLoadoutSchema:
    def __init__(self):
        ...

class VehicleOptDeviceLoadoutsModel(models.Model):
    __slots__: tuple
    vehicleId: _Any
    gold: _Any
    legend: _Any
    def __init__(self, vehicleId, gold, legend):
        ...
    def convertToView(self):
        ...
    def _parse(self, loadoutModel):
        ...
    def _determineAssistType(self, vehicleId, linkedVehicleID):
        ...

# base nao representavel no stub: Schema[...]
class VehicleOptDeviceLoadoutsSchema:
    def __init__(self):
        ...
