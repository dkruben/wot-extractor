# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/gui/Scaleform/meta/BaseContactViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/BaseContactViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseContactViewMeta(BaseDAAPIComponent):

    def onOk(self, data):
        self._printOverrideError('onOk')

    def onCancel(self):
        self._printOverrideError('onCancel')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)

    def as_setOkBtnEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setOkBtnEnabled(isEnabled)

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_closeViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeView()
