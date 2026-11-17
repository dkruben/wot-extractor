# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/sounds/vehicle_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from halloween.gui.sounds import SoundComponentBase as SoundComponentBase, playSound as playSound
from halloween_common.halloween_constants import ATTACK_REASON as ATTACK_REASON
from halloween.gui.sounds.sound_constants import BossBattleSound as BossBattleSound, HexapodBossBattleSound as HexapodBossBattleSound, BOTS_ENGINE as BOTS_ENGINE, BOTS_EXPLOSION as BOTS_EXPLOSION, VehicleSoulsContainerSounds as SoulsSounds
from HWBuffBossAuraComponent import HWBuffBossAuraComponent as HWBuffBossAuraComponent

class HWBossBattleSounds(SoundComponentBase):
    _APPLIABLE_ATTACK_REASONS: tuple
    _INVULNERABLE_ATTACK_REASONS: tuple
    _arenaBonusType: Any
    def __init__(self, parent):
        ...
    def onAvatarReady(self):
        ...
    def onBossDamageReceived(self, attackerID, attackReason, damage):
        ...
    def _containsAuraComponent(self):
        ...

class HWHexapodBossBattleSounds(HWBossBattleSounds):
    _FIRE_COOLDOWN = 1.0
    _RELOAD_WARNING_TIME = 2.0
    _id: Any
    _shotTime: Any
    def __init__(self, parent):
        ...
    def onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def _onVehicleShot(self, vehicleID):
        ...

class HWCommonEnemySounds(SoundComponentBase):
    def onAvatarReady(self):
        ...
    def onVehicleKilled(self, victimID, *_):
        ...

class HWSoulsContainerSounds(SoundComponentBase):
    _souls: Any
    def __init__(self, parent):
        ...
    def onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def _onVehicleSoulsChanged(self, souls, reason):
        ...
