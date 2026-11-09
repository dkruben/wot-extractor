# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/finish_sound_player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from helpers import dependency as dependency
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener as IBattleFieldListener
from gui.battle_control.controllers.team_bases_ctrl import ITeamBasesListener as ITeamBasesListener
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_BATTLE_END_SOUND_TIME = 2

class _SOUND_EVENTS(object):
    LAST_KILL = 'end_battle_last_kill'
    BASE_CAPTURED = 'end_battle_capture_base'
    TIME_IS_OVER = 'time_over'

class FinishSoundPlayer(IBattleFieldListener, ITeamBasesListener, IAbstractPeriodView):
    sessionProvider: Any
    __isPlaying: Any
    __vehCheckAllowed: Any
    _arenaPeriod: Any
    _arenaTotalTime: Any
    def __init__(self):
        ...
    def updateDeadVehicles(self, aliveAllies, deadAllies, aliveEnemies, deadEnemies):
        ...
    def setTeamBaseCaptured(self, clientID, playerTeam):
        ...
    def addCapturedTeamBase(self, clientID, playerTeam, timeLeft, invadersCnt):
        ...
    def setPeriod(self, period):
        ...
    def setTotalTime(self, totalTime):
        ...
    def _playSound(self, soundID):
        ...
    def _checkTimeCondition(self):
        ...
    def _playRoundFinished(self, soundID):
        ...
