# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionFirstEntryViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionFirstEntryViewMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionFirstEntryViewMeta(View):

    def playVideo(self):
        self._printOverrideError('playVideo')

    def backBtnClicked(self):
        self._printOverrideError('backBtnClicked')

    def onViewClose(self, isAcceptBtnClick):
        self._printOverrideError('onViewClose')

    def onCardClick(self, cardID):
        self._printOverrideError('onCardClick')

    def onNextCardClick(self, cardID):
        self._printOverrideError('onNextCardClick')

    def onPrevCardClick(self, cardID):
        self._printOverrideError('onPrevCardClick')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setDetailedCardDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDetailedCardData(data)
