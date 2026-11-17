# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shared/fitting_select/module_extenders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS as UI_STORAGE_KEYS, ServerSettingsManager as ServerSettingsManager
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils import TURBOSHAFT_ENGINE_POWER as TURBOSHAFT_ENGINE_POWER, ROCKET_ACCELERATION_ENGINE_POWER as ROCKET_ACCELERATION_ENGINE_POWER, CONTINUOUS_SHOTS_PER_MINUTE as CONTINUOUS_SHOTS_PER_MINUTE
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from gui.shared.gui_items.vehicle_modules import VehicleEngine as VehicleEngine, VehicleGun as VehicleGun
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from gui.shared.gui_items.vehicle_modules import VehicleModule as VehicleModule
_ModuleParamExtendInfo: Any

class ModuleParamsExtender(object):
    __slots__: tuple
    __settingsUpdated: Any
    __settingsKey: Any
    def __init__(self, settingsKey):
        ...
    def check(self, vehicleModule, vehicleDescriptor):
        ...
    def highlightCheck(self, settings):
        ...
    def updatedHighlightSettings(self, settings):
        ...
    def extendParamList(self, paramList):
        ...

class ReplaceModuleParamsExtender(ModuleParamsExtender):
    __slots__: tuple
    __replaceInfo: Any
    def __init__(self, settingsKey, replaceInfo):
        ...
    def extendParamList(self, paramList):
        ...

class AutoReloadParamsExtender(ReplaceModuleParamsExtender):
    def __init__(self):
        ...
    def check(self, vehicleModule, vehicleDescriptor):
        ...
    def highlightCheck(self, settings):
        ...

class AutoShootParamsExtender(ReplaceModuleParamsExtender):
    def __init__(self):
        ...
    def check(self, vehicleModule, vehicleDescriptor):
        ...
    def highlightCheck(self, settings):
        ...

class DualGunParamsExtender(ReplaceModuleParamsExtender):
    def __init__(self):
        ...
    def check(self, vehicleModule, vehicleDescriptor):
        ...
    def highlightCheck(self, settings):
        ...

class TurboshaftParamsExtender(ModuleParamsExtender):
    def __init__(self):
        ...
    def highlightCheck(self, settings):
        ...
    def check(self, vehicleModule, vehicleDescriptor):
        ...
    def extendParamList(self, paramList):
        ...

class RocketAccelerationParamsExtender(ModuleParamsExtender):
    def __init__(self):
        ...
    def highlightCheck(self, settings):
        ...
    def check(self, vehicleModule, vehicleDescriptor):
        ...
    def extendParamList(self, paramList):
        ...

def fittingSelectModuleExtenders():
    ...
