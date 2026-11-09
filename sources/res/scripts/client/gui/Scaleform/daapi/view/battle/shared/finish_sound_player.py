# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/finish_sound_player.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/finish_sound_player.py
from __future__ import absolute_import
import SoundGroups
from constants import ARENA_PERIOD
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from helpers import dependency
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener
from gui.battle_control.controllers.team_bases_ctrl import ITeamBasesListener
from skeletons.gui.battle_session import IBattleSessionProvider
_BATTLE_END_SOUND_TIME = 2

class _SOUND_EVENTS(object):
    LAST_KILL = 'end_battle_last_kill'
    BASE_CAPTURED = 'end_battle_capture_base'
    TIME_IS_OVER = 'time_over'


class FinishSoundPlayer(IBattleFieldListener, ITeamBasesListener, IAbstractPeriodView):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(FinishSoundPlayer, self).__init__()
        self.__isPlaying = False
        self.__vehCheckAllowed = not self.sessionProvider.arenaVisitor.isArenaFogOfWarEnabled()
        self._arenaPeriod = None
        self._arenaTotalTime = None
        return

    def updateDeadVehicles(self, aliveAllies, deadAllies, aliveEnemies, deadEnemies):
        if self.__vehCheckAllowed:
            allies = aliveAllies | deadAllies
            enemies = aliveEnemies | deadEnemies
            if allies and deadAllies == allies or enemies and deadEnemies == enemies:
                self._playRoundFinished(_SOUND_EVENTS.LAST_KILL)

    def setTeamBaseCaptured(self, clientID, playerTeam):
        self._playRoundFinished(_SOUND_EVENTS.BASE_CAPTURED)

    def addCapturedTeamBase(self, clientID, playerTeam, timeLeft, invadersCnt):
        self._playRoundFinished(_SOUND_EVENTS.BASE_CAPTURED)

    def setPeriod(self, period):
        self._arenaPeriod = period

    def setTotalTime(self, totalTime):
        self._arenaTotalTime = totalTime
        self._checkTimeCondition()

    def _playSound(self, soundID):
        SoundGroups.g_instance.playSound2D(soundID)

    def _checkTimeCondition(self):
        if self._arenaPeriod == ARENA_PERIOD.BATTLE and self._arenaTotalTime == _BATTLE_END_SOUND_TIME:
            self._playRoundFinished(_SOUND_EVENTS.TIME_IS_OVER)

    def _playRoundFinished(self, soundID):
        if not self.__isPlaying:
            self._playSound(soundID)
            self.__isPlaying = True
