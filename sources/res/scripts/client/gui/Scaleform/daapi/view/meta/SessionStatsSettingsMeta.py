# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/SessionStatsSettingsMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SessionStatsSettingsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SessionStatsSettingsMeta(BaseDAAPIComponent):

    def onClickApplyBtn(self):
        self._printOverrideError('onClickApplyBtn')

    def onClickBackBtn(self):
        self._printOverrideError('onClickBackBtn')

    def onClickResetBtn(self):
        self._printOverrideError('onClickResetBtn')

    def onSettingsInputChanged(self, identifier, value):
        self._printOverrideError('onSettingsInputChanged')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setControlsStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsState(data)

    def as_setBattleSettingsStatusS(self, value, showWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleSettingsStatus(value, showWarning)
