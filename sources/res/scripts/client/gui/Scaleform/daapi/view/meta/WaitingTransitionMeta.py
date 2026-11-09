# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/WaitingTransitionMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WaitingTransitionMeta.py
from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class WaitingTransitionMeta(DAAPISimpleContainerMeta):

    def as_setTransitionTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setTransitionText(text)

    def as_updateStageS(self, width, height, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(width, height, scale)

    def as_showBGS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBG()

    def as_hideBGS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBG()
