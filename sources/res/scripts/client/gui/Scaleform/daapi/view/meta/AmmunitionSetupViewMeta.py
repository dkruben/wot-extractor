# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionSetupViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionSetupViewMeta.py
from gui.Scaleform.framework.entities.View import View

class AmmunitionSetupViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def as_gfSizeUpdatedS(self, x, width, bottomMargin):
        if self._isDAAPIInited():
            return self.flashObject.as_gfSizeUpdated(x, width, bottomMargin)

    def as_showCloseAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showCloseAnim()

    def as_onAnimationEndS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onAnimationEnd()

    def as_toggleParamsS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleParams(isVisible)
