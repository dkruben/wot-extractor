# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/OverheatDecorativeCrosshairMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/OverheatDecorativeCrosshairMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.decorative_crosshairs.vehicle_decorative_crosshair import VehicleDecorativeCrosshair

class OverheatDecorativeCrosshairMeta(VehicleDecorativeCrosshair):

    def as_setStacksProgresS(self, progress, level):
        if self._isDAAPIInited():
            return self.flashObject.as_setStacksProgres(progress, level)

    def as_setHeatProgresS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeatProgres(progress)

    def as_updateStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_updateState(state)

    def as_setInitDataS(self, speedLimit, maxLevel, heatingTime, coolingTime, isSpeedChanged):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(speedLimit, maxLevel, heatingTime, coolingTime, isSpeedChanged)

    def as_setDamageDataS(self, baseDamage, maxDamage):
        if self._isDAAPIInited():
            return self.flashObject.as_setDamageData(baseDamage, maxDamage)
