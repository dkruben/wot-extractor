# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/vehicle_modifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import copy as copy
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from battle_modifiers_common import ModifiersContext as ModifiersContext
from battle_modifiers_common.battle_modifiers import BattleParams as BattleParams
from battle_modifiers_ext.constants_ext import USE_VEHICLE_CACHE as USE_VEHICLE_CACHE, MAX_VEHICLE_CACHE_LAYER_COUNT as MAX_VEHICLE_CACHE_LAYER_COUNT, DEBUG_MODIFIERS as DEBUG_MODIFIERS, ModifierDomain as ModifierDomain
from battle_modifiers_ext.modification_cache.modification_cache import ModificationCache as ModificationCache
from constants import IS_CELLAPP as IS_CELLAPP, IS_CLIENT as IS_CLIENT, SHELL_TYPES as SHELL_TYPES, SHELL_MECHANICS_TYPE as SHELL_MECHANICS_TYPE, VEHICLE_MODE as VEHICLE_MODE
from math import tan as tan, atan as atan, cos as cos, acos as acos
from items.components.chassis_components import TrackPair as TrackPair
from items.components.component_constants import DEFAULT_GUN_CLIP as DEFAULT_GUN_CLIP, DEFAULT_GUN_BURST as DEFAULT_GUN_BURST, DEFAULT_GUN_AUTORELOAD as DEFAULT_GUN_AUTORELOAD, DEFAULT_GUN_DUALGUN as DEFAULT_GUN_DUALGUN, KMH_TO_MS as KMH_TO_MS, MS_TO_KMH as MS_TO_KMH, DEFAULT_GUN_AUTOSHOOT as DEFAULT_GUN_AUTOSHOOT, DynamicShotEffect as DynamicShotEffect, ZERO_FLOAT as ZERO_FLOAT, DEFAULT_GUN_TWINGUN as DEFAULT_GUN_TWINGUN, INVALID_EFFECT_INDEX as INVALID_EFFECT_INDEX, DEFAULT_GUN_DUAL_ACCURACY as DEFAULT_GUN_DUAL_ACCURACY
from items.components.shell_components import createShellType as createShellType
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional, Type as Type, Dict as Dict, Tuple as Tuple, List as List
from Math import Vector2 as Vector2
from debug_utils import LOG_DEBUG as LOG_DEBUG
from items.vehicles import VehicleType as VehicleType
from items.vehicle_items import Chassis as Chassis, Turret as Turret, Gun as Gun, Radio as Radio, Shell as Shell, Engine as Engine, Hull as Hull, FuelTank as FuelTank
from items.components.gun_components import GunShot as GunShot
from items.components.shell_components import ShellType as ShellType
from battle_modifiers_ext.battle_modifiers import BattleModifiers as BattleModifiers
from battle_modifiers_common import BATTLE_MODIFIERS_TYPE as BATTLE_MODIFIERS_TYPE
g_cache = None

class VehicleModifier(object):
    @classmethod
    def modifyVehicle(cls, vehType, modifiers):
        ...
    @classmethod
    def _modifyVehType(cls, vehType, modifiers):
        ...
    @classmethod
    def __modifyChassis(cls, chassis, modifiers):
        ...
    @classmethod
    def __modifyTurret(cls, turret, modifiers):
        ...
    @classmethod
    def __modifyGun(cls, gun, modifiers):
        ...
    @classmethod
    def __modifyShot(cls, gun, shot, modifiers):
        ...
    @classmethod
    def __modifyShell(cls, gun, shell, modifiers):
        ...
    @classmethod
    def __modifyShellType(cls, gun, shell, shellType, modifiers):
        ...
    @classmethod
    def __modifyRadio(cls, radio, modifiers):
        ...
    @classmethod
    def __modifyEngine(cls, engine, modifiers):
        ...
    @classmethod
    def __modifyHull(cls, hull, modifiers):
        ...
    @classmethod
    def __modifyFuelTanks(cls, fuelTank, modifiers):
        ...
    @classmethod
    def __modifyPhysics(cls, physics, modifiers):
        ...
    @classmethod
    def __modifyPhysicsServer(cls, physics, modifiers):
        ...
    @classmethod
    def __modifyPhysicsClient(cls, physics, modifiers):
        ...
    @classmethod
    def __modifyHullCustomEffects(cls, customEffects, modifiers):
        ...
    @classmethod
    def __modifyVehicleEffects(cls, vehEffects, modifiers):
        ...

class VehicleModificationCache(ModificationCache):
    DEFAULT_LAYER_COUNT = MAX_VEHICLE_CACHE_LAYER_COUNT
    __slots__: tuple
    def get(self, vehType, battleModifiers):
        ...
    def __addModification(self, vehType, battleModifiers):
        ...
    def __getVehId(self, vehType):
        ...

def init():
    ...
