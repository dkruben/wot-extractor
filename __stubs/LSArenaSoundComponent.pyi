# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSArenaSoundComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from constants import ARENA_PERIOD as ARENA_PERIOD
from PlayerEvents import g_playerEvents as g_playerEvents
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent
from last_stand_common.last_stand_constants import INVALID_PHASE as INVALID_PHASE
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand.gui.sounds.sound_constants import BOTS_SPAWN as BOTS_SPAWN, BATTLE_START as BATTLE_START, BATTLE_FINISH as BATTLE_FINISH, DifficultyState as DifficultyState
from last_stand.gui.sounds.arena_components import LSStaticDeathZoneSounds as LSStaticDeathZoneSounds, LSPostMortemSounds as LSPostMortemSounds, LSEquipmentPanelSounds as LSEquipmentPanelSounds, LSPersonalDeathZoneSounds as LSPersonalDeathZoneSounds, LSVoiceovers as LSVoiceovers, LSTeamFightVoiceovers as LSTeamFightVoiceovers, LSBattleMusic as LSBattleMusic, LSConvoySounds as LSConvoySounds
from last_stand.gui.sounds import playSound as playSound, ComponentsHolder as ComponentsHolder
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_ARENA_SOUND_COMPONENTS: list
_PHASE_END_WARNING_TIME_OFFSET = 62
_PHASE_END_WARNING_TIME_OFFSET_DELTA = 2
_LS_MODE_WORLD = 1

class LSArenaSoundComponent(DynamicScriptComponent):
    _sessionProvider: Any
    _components: Any
    _shouldTriggerPhaseEndWarningEvent: Any
    def __init__(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def onBotCreated(self, vehicleType, position):
        ...
    def _onPhaseChanged(self, arenaPhases):
        ...
    def _setPhaseStates(self, activePhase):
        ...
    def _onPhaseTimeChanged(self, timeLeft, _, lastPhase, isTimerAlarmEnabled):
        ...
    def _onArenaPeriodChaned(self, period, *_):
        ...
