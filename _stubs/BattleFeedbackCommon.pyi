# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/BattleFeedbackCommon.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ATTACK_REASON as ATTACK_REASON, ATTACK_REASON_INDICES as ATTACK_REASON_INDICES
BATTLE_EVENTS_PROCESSING_TIMEOUT = 0.2
CAPTURE_POINTS_TO_REPORT = 10
CAPTURE_BLOCKED_SESSION_TIMEOUT = 3
CAPTURE_BLOCKED_POINTS_TO_REPORT = 10
NONE_SHELL_TYPE = 127

class BATTLE_EVENT_TYPE:
    SPOTTED = 0
    RADIO_ASSIST = 1
    TRACK_ASSIST = 2
    BASE_CAPTURE_POINTS = 3
    BASE_CAPTURE_DROPPED = 4
    TANKING = 5
    CRIT = 6
    DAMAGE = 7
    KILL = 8
    RECEIVED_CRIT = 9
    RECEIVED_DAMAGE = 10
    STUN_ASSIST = 11
    TARGET_VISIBILITY = 12
    ENEMY_SECTOR_CAPTURED = 13
    DESTRUCTIBLE_DAMAGED = 14
    DESTRUCTIBLE_DESTROYED = 15
    DESTRUCTIBLES_DEFENDED = 16
    DEFENDER_BONUS = 17
    SMOKE_ASSIST = 18
    INSPIRE_ASSIST = 19
    BASE_CAPTURE_BLOCKED = 20
    MULTI_STUN = 21
    DETECTED = 22
    EQUIPMENT_TIMER_EXPIRED = 23
    VEHICLE_HEALTH_ADDED = 24
    HIDE_IF_TARGET_INVISIBLE: tuple
    DISCLOSED_ATTACK_REASON_IDS: tuple
    DAMAGE_EVENTS: Any
    CRITS_EVENTS: Any
    TARGET_EVENTS: Any
    POINTS_EVENTS: Any
    VISIBILITY_EVENTS: Any
    STUN_EVENTS: Any
    TARGET_POINTS_EVENTS: Any
    EQUIPMENT_EVENTS: Any
    ALL: Any
    @staticmethod
    def packDamage(damage, attackReasonID, isBurst=False, shellTypeID=..., shellIsGold=False, secondaryAttackReasonID=..., isRoleAction=False, isAutoShoot=False, attackReasonExtID=-1, attackerMechanicShotMode=0):
        ...
    @staticmethod
    def unpackDamage(packedDamage):
        ...
    @staticmethod
    def unpackEntityDamage(packedDamage):
        ...
    @staticmethod
    def unpackAttackReason(packedDamage):
        ...
    @staticmethod
    def packCrits(critsCount, attackReasonID, shellTypeID=..., shellIsGold=False, secondaryAttackReasonID=..., isAutoShoot=False, attackReasonExtID=-1, attackerMechanicShotMode=0):
        ...
    @staticmethod
    def unpackCrits(packedCrits):
        ...
    @staticmethod
    def packVisibility(isVisible, isDirect, isRoleAction):
        ...
    @staticmethod
    def unpackVisibility(packedVisibility):
        ...

def _toSignedInt(value, mask):
    ...
