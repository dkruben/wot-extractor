# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/VSPlanEvents.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from typing import Optional as Optional
OnInnerDeviceWasCrit: Any
OnVehicleEquipmentActivated: Any
OnVehicleTotalDamageDealtIncrease: Any
OnVehicleAssistIncrease: Any
OnVehicleBlockDamage: Any
OnVehicleInRange: Any
OnVehicleShotDamagedEnemyVehicle: Any
OnVehicleRadioDistanceChange: Any
OnWitnessEnemyDamaged: Any
OnTankmanStatusChanged: Any

class PcVSPlanSimpleEvent(object):
    CLIENT_ACTIVATION_EVENT = 'OnClientActivation'
    VEHICLE_START_MOVING = 'OnVehicleStartMoving'
    VEHICLE_STOP_MOVING = 'OnVehicleStopMoving'
    VEHICLE_START_FWD_MOVING = 'OnVehicleStartFwdMoving'
    VEHICLE_STOP_FWD_MOVING = 'OnVehicleStopFwdMoving'
    VEHICLE_SHOOT = 'OnVehicleShoot'
    VEHICLE_STUN = 'OnVehicleStun'
    VEHICLE_STUN_OFF = 'OnVehicleStunOff'
    VEHICLE_FIRE_STARTED = 'OnVehicleFireStarted'
    VEHICLE_FIRE_STOPPED = 'OnVehicleFireStopped'
    VEHICLE_EQUIPMENT_SWAP = 'OnVehicleEquipmentSwap'
    VEHICLE_DAMAGE_BY_ENEMY = 'OnVehicleDamageByEnemy'
    VEHICLE_DAMAGE_RECEIVED = 'onVehicleDamageReceived'
    VEHICLE_CHANGE_HEALTH = 'OnVehicleChangeHealth'
    VEHICLE_DEVICE_WAS_CRIT = 'OnVehicleDeviceWasCrit'
    VEHICLE_TANKMAN_WAS_CRIT = 'OnVehicleTankmanWasCrit'
    VEHICLE_TANKMAN_HEALED = 'OnVehicleTankmanHealed'
    VEHICLE_DEVICE_HEALED = 'OnVehicleDeviceHealed'
    VEHICLE_GUN_REALOAD_FINISHED = 'OnVehicleGunReloadFinished'
    VEHICLE_CLIP_REALOAD_FINISH = 'OnVehicleClipReload'
    ENEMY_DETECTED = 'OnEnemyDetected'
    VEHICLE_SIXTH_SENSE_ACTIVATE = 'OnVehicleSixthSenseActivate'
    VEHICLE_CHANGE_SHELLS_BY_CLIENT = 'OnVehicleChangeShellsByClient'
    VEHICLE_ON_TARGET_KILLED = 'OnVehicleOnTargetKilled'
    VEHICLE_ON_TARGET_CRIT = 'OnVehicleOnTargetCrit'
    ARENA_ON_BATTLE_START = 'OnArenaOnBattleStart'
    ON_NO_DAMAGE_SHOT = 'OnNoDamageShot'

class VSPlanEventPerkData(object):
    __slots__: tuple
    perkID: Any
    def __init__(self):
        ...
    def __str__(self):
        ...
