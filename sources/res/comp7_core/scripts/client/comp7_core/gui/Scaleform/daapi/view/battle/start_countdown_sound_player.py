# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/start_countdown_sound_player.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/start_countdown_sound_player.py
from __future__ import absolute_import
from constants import VEHICLE_SELECTION_BLOCK_DELAY
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer
from gui.battle_control.battle_constants import COUNTDOWN_STATE

class Comp7StartTimerSoundPlayer(StartCountdownSoundPlayer):

    def setCountdown(self, state, timeLeft):
        correctedTimeLeft = timeLeft - VEHICLE_SELECTION_BLOCK_DELAY if timeLeft is not None else timeLeft
        if correctedTimeLeft < 0:
            state = COUNTDOWN_STATE.STOP
        super(Comp7StartTimerSoundPlayer, self).setCountdown(state, correctedTimeLeft)
        return
