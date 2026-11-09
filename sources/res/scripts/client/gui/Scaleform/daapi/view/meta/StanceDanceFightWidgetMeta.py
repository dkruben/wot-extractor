# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/StanceDanceFightWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StanceDanceFightWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StanceDanceFightWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, isSwitchingState, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(isSwitchingState, progress)

    def as_energyBoostS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_energyBoost()

    def as_switchTimerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchTimer(value)

    def as_keysVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_keysVisible(value)

    def as_pauseReplayS(self, isPaused):
        if self._isDAAPIInited():
            return self.flashObject.as_pauseReplay(isPaused)
