# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/renewable_subscription_common/optional_devices_usage_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from enum import Enum as Enum
from future.utils import lmap as lmap, viewitems as viewitems
from items import vehicles as vehicles
from renewable_subscription_common.settings_constants import OptionalDevicesUsageConst as OptionalDevicesUsageConst
from soft_exception import SoftException as SoftException
from ResMgr import DataSection as DataSection
from typing import Dict as Dict, List as List
_logger: Any
VehicleLoadout: Any
VehicleLevelClassRoleGroup: Any
EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP: dict
GENERIC_OPTIONAL_DEVICE_MAP_TO_EQUIPMENT_NAME: dict

class GenericOptionalDevice(Enum):
    STEREOSCOPE = 1
    TURBOCHARGER = 2
    ENHANCED_AIM_DRIVES = 3
    GROUSERS = 4
    AIMING_STABILIZER = 5
    ANTIFRAGMENTATION_LINING = 6
    CAMOUFLAGE_NET = 7
    IMPROVED_SIGHTS = 8
    VENTILATION = 9
    HEALTH_RESERVE = 10
    ROTATION_MECHANISM = 11
    RAMMER = 12
    COATED_OPTICS = 13
    ADDIT_INVISIBILITY_DEVICE = 14
    IMPROVED_CONFIGURATION = 15
    RADIO_COMMUNICATION = 16
    COMMANDERS_VIEW = 17
    MODERNIZED_EXTRA_HEALTH_RESERVE_ANTIFRAGMENTATION_LINING = 18
    MODERNIZED_TURBOCHARGER_ROTATION_MECHANISM = 19
    MODERNIZED_AIM_DRIVES_AIMING_STABILIZER = 20
    MODERNIZED_IMPROVED_SIGHTS_ENHANCED_AIM_DRIVES = 21

def _readOptionalDevicesUsage(section):
    ...
def _parseDevicesLoadouts(reader):
    ...
def _getVehicleTypeCompDescr(vehicleName):
    ...
def convertServerDiffToRichTypes(configDict):
    ...
def _validateOverrideConfig(configDict):
    ...
