# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/DeathCamHudMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DeathCamHudMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DeathCamHudMeta(BaseDAAPIComponent):

    def onAnimationFinished(self):
        self._printOverrideError('onAnimationFinished')

    def as_setTextsS(self, cameraText, skipText):
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(cameraText, skipText)

    def as_showBarsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBars()

    def as_hideBarsS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBars(isActive)
