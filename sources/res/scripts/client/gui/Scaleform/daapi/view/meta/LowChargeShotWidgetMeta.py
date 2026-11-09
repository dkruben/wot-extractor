# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/LowChargeShotWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LowChargeShotWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class LowChargeShotWidgetMeta(VehicleMechanicWidget):

    def as_setInitialTimeS(self, baseTime, lowChargeTime, almostFinishedTime, lowChargeCap, shellChangeTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitialTime(baseTime, lowChargeTime, almostFinishedTime, lowChargeCap, shellChangeTime)

    def as_setTimeLeftS(self, timeLeft, state, isReplay):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeLeft(timeLeft, state, isReplay)
