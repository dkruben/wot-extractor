# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionsOperationAwardsScreenMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionsOperationAwardsScreenMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionsOperationAwardsScreenMeta(View):

    def onCloseWindow(self):
        self._printOverrideError('onCloseWindow')

    def onPlaySound(self, soundType):
        self._printOverrideError('onPlaySound')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setAwardDataS(self, awardData):
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardData(awardData)

    def as_setCloseBtnEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseBtnEnabled(enabled)

    def as_playAwardsAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playAwardsAnimation()
