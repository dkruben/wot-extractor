# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PropellantGunWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PropellantGunWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class PropellantGunWidgetMeta(VehicleMechanicWidget):

    def as_setChargeValuesS(self, chargeProgress, chargeDamage):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeValues(chargeProgress, chargeDamage)

    def as_setupThresholdS(self, chargeThreshold):
        if self._isDAAPIInited():
            return self.flashObject.as_setupThreshold(chargeThreshold)

    def as_showHotKeysS(self, isShow=True):
        if self._isDAAPIInited():
            return self.flashObject.as_showHotKeys(isShow)

    def as_activateHotKeyS(self, command):
        if self._isDAAPIInited():
            return self.flashObject.as_activateHotKey(command)
