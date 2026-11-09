# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/DecorativeCrosshairPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DecorativeCrosshairPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.panels_common import VehicleMechanicsPanel

class DecorativeCrosshairPanelMeta(VehicleMechanicsPanel):

    def as_addDecorCrosshairS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_addDecorCrosshair(type)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)

    def as_updateCrosshairTypeS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCrosshairType(type)
