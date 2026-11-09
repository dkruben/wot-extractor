# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/RecoveryPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/RecoveryPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RecoveryPanelMeta(BaseDAAPIComponent):

    def as_updateTimerS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(time)

    def as_displayHintS(self, display, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_displayHint(display, animate)

    def as_displayCooldownS(self, display, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_displayCooldown(display, animate)

    def as_setupTextsS(self, hint1, hint2, button):
        if self._isDAAPIInited():
            return self.flashObject.as_setupTexts(hint1, hint2, button)

    def as_updateTextsS(self, button):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTexts(button)
