# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/WidgetsPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WidgetsPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.panels_common import VehicleMechanicsPanel

class WidgetsPanelMeta(VehicleMechanicsPanel):

    def as_addWidgetS(self, widgetType):
        if self._isDAAPIInited():
            return self.flashObject.as_addWidget(widgetType)

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)

    def as_updateCrosshairTypeS(self, crosshairType):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCrosshairType(crosshairType)

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)

    def as_isPlayerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isPlayer(value)

    def as_isReplayS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isReplay(value)
