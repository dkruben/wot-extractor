# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AmmunitionPanelMeta(BaseDAAPIComponent):

    def showRepairDialog(self):
        self._printOverrideError('showRepairDialog')

    def showCustomization(self):
        self._printOverrideError('showCustomization')

    def toRentContinue(self):
        self._printOverrideError('toRentContinue')

    def showChangeNation(self):
        self._printOverrideError('showChangeNation')

    def showEasyTankEquip(self):
        self._printOverrideError('showEasyTankEquip')

    def as_setMaintenanceWarningStateS(self, stateWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenanceWarningState(stateWarning)

    def as_highlightEasyTankEquipS(self, isHighlight):
        if self._isDAAPIInited():
            return self.flashObject.as_highlightEasyTankEquip(isHighlight)

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)

    def as_setCustomizationBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCustomizationBtnCounter(value)
