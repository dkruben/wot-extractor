# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/EpicPrimeTimeMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicPrimeTimeMeta.py
from gui.Scaleform.daapi.view.lobby.prime_time_view_base import PrimeTimeViewBase

class EpicPrimeTimeMeta(PrimeTimeViewBase):

    def as_setHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderText(value)

    def as_setBackgroundSourceS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackgroundSource(source)

    def as_setFullscreenModeSupportedS(self, isSupported):
        if self._isDAAPIInited():
            return self.flashObject.as_setFullscreenModeSupported(isSupported)

    def as_setCloseBtnVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseBtnVisibility(isVisible)

    def as_setShadowVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setShadowVisibility(isVisible)
