# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWVehicleSoundComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from halloween_common.halloween_constants import BOSS_ROLE_TAG as BOSS_ROLE_TAG, PLAYERS_TEAM as PLAYERS_TEAM, ATTACK_REASON as ATTACK_REASON, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from halloween.gui.sounds import ComponentsHolder as ComponentsHolder
from halloween.gui.sounds.vehicle_components import HWBossBattleSounds as HWBossBattleSounds, HWCommonEnemySounds as HWCommonEnemySounds, HWSoulsContainerSounds as HWSoulsContainerSounds, HWHexapodBossBattleSounds as HWHexapodBossBattleSounds
from halloween.gui.sounds.sound_constants import VEHICLE_OBJ_NAME_PATTERN as VEHICLE_OBJ_NAME_PATTERN
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_VEHICLE_SOUND_COMPONENTS: list

class HWVehicleSoundComponent(DynamicScriptComponent):
    sessionProvider: Any
    _components: Any
    _soundObject: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    @property
    def soundObject(self):
        ...
    @property
    def isBoss(self):
        ...
    @property
    def isEnemy(self):
        ...
    @property
    def hwSoulsContainer(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    @property
    def arena(self):
        ...
    def _onAvatarReady(self):
        ...
    def onBossDamageReceived(self, attackerID, attackReasonID, damage):
        ...
    def _onVehicleKilled(self, victimID, *args):
        ...
    def _onBossLivesChanged(self):
        ...
    @property
    def _arenaSoundComponent(self):
        ...
