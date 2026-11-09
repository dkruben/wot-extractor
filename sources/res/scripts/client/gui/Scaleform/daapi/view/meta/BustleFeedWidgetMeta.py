# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BustleFeedWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BustleFeedWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class BustleFeedWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, progress, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress, time)

    def as_setLockS(self, isLocked):
        if self._isDAAPIInited():
            return self.flashObject.as_setLock(isLocked)

    def as_setAvailabilityS(self, isDisable):
        if self._isDAAPIInited():
            return self.flashObject.as_setAvailability(isDisable)

    def as_setCommandS(self, command):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommand(command)
