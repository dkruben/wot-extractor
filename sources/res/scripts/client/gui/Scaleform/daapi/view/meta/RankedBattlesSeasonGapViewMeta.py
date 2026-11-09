# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesSeasonGapViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesSeasonGapViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesSeasonGapViewMeta(BaseDAAPIComponent):

    def onBtnClick(self):
        self._printOverrideError('onBtnClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setEfficiencyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEfficiencyData(data)

    def as_setRatingDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRatingData(data)
