# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ChargeShotWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ChargeShotWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class ChargeShotWidgetMeta(VehicleMechanicWidget):

    def as_setUpdateProgressS(self, stack, progressValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setUpdateProgress(stack, progressValue)

    def as_setShootBlockS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShootBlock(value)

    def as_setDamageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDamage(value)

    def as_showShootBlockAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showShootBlockAnimation()
