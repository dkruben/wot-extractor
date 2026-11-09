# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/start_countdown_sound_player.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/start_countdown_sound_player.py
from __future__ import absolute_import
import logging, WWISE
from helpers import dependency
import BattleReplay
from gui.battle_control.battle_constants import COUNTDOWN_STATE
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.battle_control.view_components import IViewComponentsCtrlListener
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)
_RTPC = 'RTPC_ext_battle_countdown_timer'

class StartCountdownSoundPlayer(IAbstractPeriodView, IViewComponentsCtrlListener):

    def __init__(self):
        super(StartCountdownSoundPlayer, self).__init__()
        self.__soundID = dependency.instance(IBattleSessionProvider).arenaVisitor.type.getCountdownTimerSound()
        if not self.__soundID:
            _logger.warning('Countdown sound for this game mode is not defined! Define or remove player from page')

    def setCountdown(self, state, timeLeft):
        if state == COUNTDOWN_STATE.START:
            self.__updateSound(timeLeft)

    def __updateSound(self, timeLeft):
        if self.__checkNotReplay():
            self.__playSound(timeLeft)

    def __checkNotReplay(self):
        replay = BattleReplay.g_replayCtrl
        if replay.isPlaying:
            return replay.playbackSpeed != 0
        return True

    def __playSound(self, timeLeft):
        if self.__soundID:
            WWISE.WW_setRTCPGlobal(_RTPC, timeLeft)
            WWISE.WW_eventGlobal(self.__soundID)
