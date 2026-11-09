# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/sounds/voiceovers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/sounds/voiceovers.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency
from halloween.gui.sounds import playSound
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController
from halloween.gui.halloween_account_settings import isSoundPlayed, setSoundPlayed
from gui.battle_control.avatar_getter import getSoundNotifications
from gui.IngameSoundNotifications import LOG_VO

class Voiceover(object):
    _difficultyCtrl = dependency.descriptor(IDifficultyLevelController)

    def __init__(self, standardVoiceover, expositionVoiceover=None, useNotificationSystem=True, aliveOnly=False):
        self._standardVoiceover = standardVoiceover
        self._expositionVoiceover = expositionVoiceover
        self._useNotificationSystem = useNotificationSystem
        self._aliveOnly = aliveOnly

    def play(self):
        if self._aliveOnly and not BigWorld.player().isVehicleAlive:
            LOG_VO(('HW Request "{}" is rejected. Reason: player is dead').format(self._standardVoiceover))
            return
        else:
            voiceover = self._standardVoiceover
            if self._expositionVoiceover is not None:
                difficultyLevel = self._difficultyCtrl.getSelectedLevel()
                if not isSoundPlayed(self._expositionVoiceover, difficultyLevel):
                    voiceover = self._expositionVoiceover
                    setSoundPlayed(self._expositionVoiceover, difficultyLevel)
            if voiceover:
                if self._useNotificationSystem:
                    soundNotifications = getSoundNotifications()
                    if soundNotifications and hasattr(soundNotifications, 'play'):
                        soundNotifications.play(voiceover)
                else:
                    playSound(voiceover)
            return
