# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ChargeableBurstWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ChargeableBurstWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class ChargeableBurstWidgetMeta(VehicleMechanicWidget):

    def as_setupS(self, penetrationCount, burstShootCount):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(penetrationCount, burstShootCount)

    def as_setModeS(self, isBurstMode, isInstantly):
        if self._isDAAPIInited():
            return self.flashObject.as_setMode(isBurstMode, isInstantly)

    def as_setChargesS(self, charges, burstShotCount, isInstantly):
        if self._isDAAPIInited():
            return self.flashObject.as_setCharges(charges, burstShotCount, isInstantly)

    def as_setShellsQuantityLeftS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setShellsQuantityLeft(count)

    def as_updateBurstReloadingStateS(self, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBurstReloadingState(isReloading)
