# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/strongholds/sound_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/strongholds/sound_controller.py
from __future__ import absolute_import
from gui.app_loader import sf_lobby
from gui.shared.SoundEffectsId import SoundEffectsId

class _StrongholdSoundController(object):

    @sf_lobby
    def app(self):
        return

    def init(self):
        pass

    def fini(self):
        pass

    def playBattleRoomTimerAlert(self):
        self.__playSound(SoundEffectsId.BATTLE_ROOM_TIMER_ALERT)

    def __playSound(self, soundID):
        app = self.app
        if app is not None and app.soundManager is not None:
            app.soundManager.playEffectSound(soundID)
        return


g_strongholdSoundController = _StrongholdSoundController()
