# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/sounds/abstract.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/abstract.py
from gui.sounds.sound_constants import SoundSystems, SPEAKERS_CONFIG

class SoundSystemAbstract(object):

    def getID(self):
        raise NotImplementedError

    def init(self):
        pass

    def fini(self):
        pass

    def isMSR(self):
        return False

    def enableDynamicPreset(self):
        pass

    def disableDynamicPreset(self):
        pass

    def setSoundSystem(self, value):
        pass

    def setBassBoost(self, isEnabled):
        pass

    def getSystemSpeakersPresetID(self):
        return SPEAKERS_CONFIG.AUTO_DETECTION

    def getUserSpeakersPresetID(self):
        return SPEAKERS_CONFIG.AUTO_DETECTION

    def setUserSpeakersPresetID(self, presetID):
        pass

    def sendGlobalEvent(self, eventName, **params):
        pass

    def onEnvStart(self, environment):
        pass

    def onEnvStop(self, environment):
        pass

    def __repr__(self):
        return 'SoundSystem(%s)' % SoundSystems.getUserName(self.getID())
