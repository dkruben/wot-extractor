# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/vehicle_components/nitro.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import logging as logging
import typing as typing
import CGF as CGF
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_modules.variable_components import VariableStorageComponent as VariableStorageComponent
from CustomEffectManager import CustomEffectManager as CustomEffectManager
from typing import Optional as Optional
VehAccessorType: Any
EffectMgrAccessorType: Any
VarStorageType: Any
logger: Any
NITRO_COUNT_KEY = 'vehicle/nitro/count'

class Vehicle(object):
    ...

# decorador original: @enum.unique
class NitroExhaustEffect(enum.IntEnum):
    NO_NITRO = 0
    BR_NITRO = 1
    FORSAGE_GAS = 2
    FORSAGE_DIESEL = 3

# decorador original: @registerComponent
class VehicleNitroExhaustEffectComponent(object):
    category = 'Vehicle'
    editorTitle = 'Nitro Exhaust Effect'
    domain = CGF.Domain.ClientEditor
    effect: Any
    vehicleGoUUID: Any
    effectMgrGoUUID: Any
    def __init__(self):
        ...
    def initialize(self, vehGO, effectMgrGo):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def __repr__(self):
        ...

class VehicleNitroExhaustEffectComponentSystem(CGF.System):
    NitroActivated: Any
    NitroDeactivated: Any
    NitroRemoved: Any
    VehicleVarAccess: Any
    EffectMgrAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _onNitroActivated(self, go, component, vehVarAccess, effectMgrAccess):
        ...
    def _onNitroDeactivated(self, go, component, vehVarAccess, effectMgrAccess):
        ...
    @staticmethod
    def _setNitroEffect(effectMgr, nitro):
        ...
    @staticmethod
    def _changeAppliedNitroCount(vehGo, varStorage, value):
        ...
    @staticmethod
    def _isVehicleValid(vehicle):
        ...
