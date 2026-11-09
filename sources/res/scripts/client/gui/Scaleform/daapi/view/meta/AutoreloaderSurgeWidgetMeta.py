# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/AutoreloaderSurgeWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AutoreloaderSurgeWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class AutoreloaderSurgeWidgetMeta(VehicleMechanicWidget):

    def as_setStagesProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setStagesProgress(progress)

    def as_setAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAvailable(value)

    def as_setChargeCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeCount(value)

    def as_setSectorCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setSectorCount(count)

    def as_setBoostedChargeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBoostedCharge(value)
