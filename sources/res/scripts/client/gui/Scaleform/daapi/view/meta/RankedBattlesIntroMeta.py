# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesIntroMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesIntroMeta.py
from gui.Scaleform.framework.entities.View import View

class RankedBattlesIntroMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onAcceptClick(self):
        self._printOverrideError('onAcceptClick')

    def onDetailedClick(self):
        self._printOverrideError('onDetailedClick')

    def onPlayVideoClick(self):
        self._printOverrideError('onPlayVideoClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setAlertMessageBlockDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlertMessageBlockData(data)

    def as_setBeforeSeasonBlockDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBeforeSeasonBlockData(data)
