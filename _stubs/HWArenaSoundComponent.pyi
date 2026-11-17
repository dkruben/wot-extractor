# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWArenaSoundComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import WWISE as WWISE
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from PlayerEvents import g_playerEvents as g_playerEvents
from halloween.gui.sounds.voiceovers import Voiceover as Voiceover
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from halloween_common.halloween_constants import INVALID_PHASE as INVALID_PHASE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from halloween.gui.sounds.sound_constants import BATTLE_START as BATTLE_START, ACTIVE_PHASE_RTPC as ACTIVE_PHASE_RTPC, BATTLE_FINISH as BATTLE_FINISH, PHASE_CHANGED as PHASE_CHANGED, ARENA_PHASE_END_WARNING_EVENT_PREFIX as ARENA_PHASE_END_WARNING_EVENT_PREFIX, ActivePhaseState as ActivePhaseState, DifficultyState as DifficultyState, PhaseStartedVoiceover as PhaseStartedVoiceover
from halloween.gui.sounds.arena_components import HWStaticDeathZoneSounds as HWStaticDeathZoneSounds, HWPostMortemSounds as HWPostMortemSounds, HWArenaLootSounds as HWArenaLootSounds, HWBossBattleMusic as HWBossBattleMusic, HWHexapodBossBattleMusic as HWHexapodBossBattleMusic, HWEquipmentPanelSounds as HWEquipmentPanelSounds, HWBuffsPanelSounds as HWBuffsPanelSounds, HWPersonalDeathZoneSounds as HWPersonalDeathZoneSounds, HWVoiceovers as HWVoiceovers, HWTeamFightVoiceovers as HWTeamFightVoiceovers, HWPhaseStateUpdateSounds as HWPhaseStateUpdateSounds, HWVehicleDetectorSounds as HWVehicleDetectorSounds, HWBotSpawnSounds as HWBotSpawnSounds
from halloween.gui.sounds import playSound as playSound, ComponentsHolder as ComponentsHolder
_logger: Any
_ARENA_SOUND_COMPONENTS: list
_ARENA_SOUND_COMPONENTS_CONDITIONAL: list
_SUPPORTED_END_WARNING_PHASE_IDS: tuple
_PHASE_END_WARNING_TIME_OFFSET = 62

class HWArenaSoundComponent(DynamicScriptComponent):
    _components: Any
    _shouldTriggerPhaseEndWarningEvent: Any
    _bossAuraIntersectionsCounter: Any
    _ongoingSoundsPlayed: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def onBotCreated(self, vehicleType, position):
        ...
    def onPlaySoundEvent(self, event):
        ...
    def onPlayVoiceover(self, voiceover, exposition, aliveOnly):
        ...
    def onShotAtBoss(self, attackerID, attackReason, damage):
        ...
    def onBossEnterWorld(self, bossEntity):
        ...
    @property
    def arena(self):
        ...
    def _onPhaseChanged(self, arenaPhases):
        ...
    def _setPhaseStates(self, activePhase):
        ...
    def _onPhaseTimeChanged(self, timeLeft, _, lastPhase):
        ...
    def _onArenaPeriodChaned(self, period, *_):
        ...
    def onBossAuraIntersect(self, vehicleId, entered):
        ...
