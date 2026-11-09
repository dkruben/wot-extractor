# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/CalloutPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CalloutPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalloutPanelMeta(BaseDAAPIComponent):

    def onHideCompleted(self):
        self._printOverrideError('onHideCompleted')

    def onHideStart(self):
        self._printOverrideError('onHideStart')

    def as_setDataS(self, action, vehicleType, vehicleName, leftText, rightText, keyText):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(action, vehicleType, vehicleName, leftText, rightText, keyText)

    def as_setHideDataS(self, wasAnswered, answeredAction):
        if self._isDAAPIInited():
            return self.flashObject.as_setHideData(wasAnswered, answeredAction)

    def as_setCrosshairTypeS(self, viewID):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrosshairType(viewID)
