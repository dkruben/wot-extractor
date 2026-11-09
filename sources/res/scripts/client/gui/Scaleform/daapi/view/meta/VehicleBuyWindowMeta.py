# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/VehicleBuyWindowMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleBuyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleBuyWindowMeta(AbstractWindowView):

    def submit(self, data):
        self._printOverrideError('submit')

    def stateChange(self, data):
        self._printOverrideError('stateChange')

    def selectTab(self, tabIndex):
        self._printOverrideError('selectTab')

    def onTradeInClearVehicle(self):
        self._printOverrideError('onTradeInClearVehicle')

    def as_setGoldS(self, gold):
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_setCreditsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_updateTradeOffVehicleS(self, vehicleBuyTradeOffVo):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTradeOffVehicle(vehicleBuyTradeOffVo)

    def as_setTradeInWarningMessagegeS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setTradeInWarningMessagege(message)

    def as_setStateS(self, academyEnabled, schoolEnabled, freeEnabled, submitEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(academyEnabled, schoolEnabled, freeEnabled, submitEnabled)
