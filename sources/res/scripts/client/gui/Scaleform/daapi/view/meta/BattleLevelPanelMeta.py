# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BattleLevelPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleLevelPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleLevelPanelMeta(BaseDAAPIComponent):

    def onPlaySound(self, soundType):
        self._printOverrideError('onPlaySound')

    def as_setLevelS(self, currentLevel, nextLevel, currentExperience, targetExperience):
        if self._isDAAPIInited():
            return self.flashObject.as_setLevel(currentLevel, nextLevel, currentExperience, targetExperience)

    def as_setExperienceS(self, currentExperience, targetExperience, expDiff, percent, playSound):
        if self._isDAAPIInited():
            return self.flashObject.as_setExperience(currentExperience, targetExperience, expDiff, percent, playSound)

    def as_setMaxLevelReachedS(self, levelReached):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxLevelReached(levelReached)

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()

    def as_setIsPausedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsPaused(value)

    def as_setAnimationS(self, enable):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnimation(enable)
