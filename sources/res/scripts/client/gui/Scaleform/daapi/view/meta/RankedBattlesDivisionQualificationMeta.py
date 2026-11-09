# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesDivisionQualificationMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesDivisionQualificationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesDivisionQualificationMeta(BaseDAAPIComponent):

    def as_setQualificationEfficiencyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationEfficiencyData(data)

    def as_setQualificationStepsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationStepsData(data)

    def as_setQualificationDataS(self, imageSrcSmall, imageSrcBig, isFirstEnter):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationData(imageSrcSmall, imageSrcBig, isFirstEnter)

    def as_setQualificationProgressS(self, progressTextSmall, progressTextBig, isCompleted, descr):
        if self._isDAAPIInited():
            return self.flashObject.as_setQualificationProgress(progressTextSmall, progressTextBig, isCompleted, descr)
