# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/contexts/perks_context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from future.utils import lzip as lzip
from VSPlanEvents import OnVehicleEquipmentActivated as OnVehicleEquipmentActivated, OnInnerDeviceWasCrit as OnInnerDeviceWasCrit, OnVehicleTotalDamageDealtIncrease as OnVehicleTotalDamageDealtIncrease, OnVehicleAssistIncrease as OnVehicleAssistIncrease, OnVehicleInRange as OnVehicleInRange, OnVehicleShotDamagedEnemyVehicle as OnVehicleShotDamagedEnemyVehicle, OnVehicleRadioDistanceChange as OnVehicleRadioDistanceChange, OnWitnessEnemyDamaged as OnWitnessEnemyDamaged, OnTankmanStatusChanged as OnTankmanStatusChanged, OnVehicleBlockDamage as OnVehicleBlockDamage
from items.components.perks_constants import PerkState as PerkState
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.context import VScriptContext as VScriptContext, vse_get_property as vse_get_property, vse_func_call as vse_func_call, vse_forward_event as vse_forward_event, vse_context_effect_forward_event as vse_context_effect_forward_event
from visual_script.type import VScriptEnum as VScriptEnum

class PerkNotifyState(VScriptEnum):
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...

class PerkContext(VScriptContext):
    OnVehicleStartMoving: Any
    OnVehicleStopMoving: Any
    OnVehicleStartFwdMoving: Any
    OnVehicleStopFwdMoving: Any
    OnVehicleShoot: Any
    OnVehicleStun: Any
    OnVehicleStunOff: Any
    OnVehicleFireStarted: Any
    OnVehicleFireStopped: Any
    OnVehicleEquipmentSwap: Any
    OnVehicleDamageByEnemy: Any
    onVehicleDamageReceived: Any
    OnVehicleChangeHealth: Any
    OnVehicleDeviceWasCrit: Any
    OnVehicleTankmanWasCrit: Any
    OnVehicleTankmanHealed: Any
    OnVehicleDeviceHealed: Any
    OnVehicleGunReloadFinished: Any
    OnVehicleClipReload: Any
    OnEnemyDetected: Any
    OnVehicleSixthSenseActivate: Any
    OnVehicleChangeShellsByClient: Any
    OnVehicleOnTargetKilled: Any
    OnVehicleOnTargetCrit: Any
    OnArenaOnBattleStart: Any
    OnNoDamageShot: Any
    OnInnerDeviceWasCrit: Any
    OnVehicleEquipmentActivated: Any
    OnVehicleTotalDamageDealtIncrease: Any
    OnVehicleAssistIncrease: Any
    OnVehicleBlockDamage: Any
    OnVehicleInRange: Any
    OnVehicleShotDamagedEnemyVehicle: Any
    OnWitnessEnemyDamaged: Any
    OnVehicleRadioDistanceChange: Any
    OnPerkRestarted: Any
    _aspectImpl: Any
    def __init__(self, aspectImplClass, perksControllerWeakRef, perkID, perkLevel, scopeID):
        ...
    @property
    def perkID(self):
        ...
    @property
    def perkLevel(self):
        ...
    @property
    def scopeID(self):
        ...
    @property
    def vehicleID(self):
        ...
    # decorador original: @vse_get_property(...)
    def getSelf(self):
        ...
    # decorador original: @vse_get_property(...)
    def getVehicle(self):
        ...
    # decorador original: @vse_get_property(...)
    def getArena(self):
        ...
    # decorador original: @vse_get_property(...)
    def getPerkID(self):
        ...
    # decorador original: @vse_get_property(...)
    def getLevel(self):
        ...
    # decorador original: @vse_get_property(...)
    def getVehicleID(self):
        ...
    # decorador original: @vse_func_call(...)
    def addFactorModifier(self, factor, value):
        ...
    # decorador original: @vse_func_call(...)
    def removeFactorModifiers(self, factor, numMods):
        ...
    # decorador original: @vse_func_call(...)
    def dropAllPerkModifiers(self):
        ...
    def setPerkLevel(self, level):
        ...
    # decorador original: @vse_func_call(...)
    def notifyOnClient(self, state, lifeTime):
        ...
    # decorador original: @vse_func_call(...)
    def notifyOnClientRibbon(self):
        ...

class CrewContext(PerkContext):
    _aspectImpl: Any
    # decorador original: @vse_context_effect_forward_event(...)
    def tankmanStatusChangedEffect(self, *args):
        ...
    # decorador original: @vse_get_property(...)
    def getIsActive(self):
        ...
    # decorador original: @vse_get_property(...)
    def needTankmanUpdate(self):
        ...
    # decorador original: @vse_func_call(...)
    def setAmmoChangeFactorForVehicle(self, factor):
        ...
    def __init__(self, aspectImplClass, perksControllerWeakRef, perkID, perkLevel, scopeID, skillData):
        ...
