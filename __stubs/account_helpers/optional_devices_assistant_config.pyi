# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/optional_devices_assistant_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import csv as csv
import typing as typing
from io import StringIO as StringIO
from past.builtins import unicode as unicode
import ResMgr as ResMgr
from constants import VEHICLE_CLASS_INDICES as VEHICLE_CLASS_INDICES, ROLE_LABEL_TO_TYPE as ROLE_LABEL_TO_TYPE
from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout as VehicleLoadout, EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP as EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP, _getVehicleTypeCompDescr as _getVehicleTypeCompDescr, VehicleLevelClassRoleGroup as VehicleLevelClassRoleGroup
from soft_exception import SoftException as SoftException
from typing import Dict as Dict
_USAGE_CONFIG_FILE = 'scripts/item_defs/optional_devices_assistance/optional_devices_usage.csv'
_USAGE_CONFIG_FILE_LEGENDARY: str
_FALLBACK_CONFIG_FILE: str
DEFAULT_ROLE = 'NotDefined'

def readOptionalDevicesUsageConfig(fileName):
    ...
def readOptionalDevicesUsageFallbackConfig():
    ...
def _readOptionalDevicesFallbackUsage(section):
    ...
