# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/legacy_mechanics/dualgun_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
import math_utils as math_utils
import BigWorld as BigWorld
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer

class DualGunSoundEvents(object):
    CHARGE_FX = 'gun_rld_dual_charge_FX'
    CHARGE_STARTED = 'gun_rld_dual_charge_start'
    CHARGE_CANCEL = 'gun_rld_dual_charge_cancel'
    CHARGE_FAILED = 'gun_rld_dual_charge_fail'
    CHARGE_PRE = 'gun_rld_dual_charge_pre'
    RTPC_CHARGE_PROGRESS = 'RTPC_ext_gun_rld_dual_charge_progress'
    CHARGE_PROGRESS_STOP = 'gun_rld_dual_charge_progress_loop_stop'
    COOLDOWN_END = 'gun_rld_dual_cooldown_end'
    NOT_ENOUGH_SHELLS = 'gun_rld_dual_charge_no_enough_shells'
    WEAPON_CHANGED = 'gun_rld_dual_wpn_change'
    DAULGUN_RELOAD_SNIPER_SWITCH = 'gun_rld_dual_wpn_switch_sniper_mode'
    CHARGE_SOUND_FX_LENGTH = 1.0
    WEAPON_CHANGED_SOUND_LENGTH = 1.0

class ChargeSoundRTPCInterpolator(CallbackDelayer):
    __startTime: Any
    __totalInterpolationTime: Any
    enabled: Any
    def __init__(self, interpolationTime=0.0):
        ...
    def enable(self, interpolationTime):
        ...
    def disable(self):
        ...
    def __update(self):
        ...

class DualGunSounds(CallbackDelayer):
    __interpolator: Any
    def __init__(self):
        ...
    def onComponentDisposed(self):
        ...
    def onChargeStarted(self, timeLeft):
        ...
    def onChargeCanceled(self):
        ...
    def onWeaponChanged(self, leftTime):
        ...
    def onCooldownEnd(self, leftTime):
        ...
    def onObserverSwitched(self):
        ...
    @staticmethod
    def onPreChargeStarted():
        ...
    @staticmethod
    def onChargeReleased(canShoot, error, canMakeDualShoot):
        ...
    @staticmethod
    def __runFXSound():
        ...
    @staticmethod
    def __runCooldownEndSound():
        ...
    @staticmethod
    def __runChangeWeaponSound():
        ...
