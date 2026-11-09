# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineMinimapMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineMinimapMeta.py
from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent

class FrontlineMinimapMeta(MinimapComponent):

    def onZoomModeChanged(self, change):
        self._printOverrideError('onZoomModeChanged')

    def as_setZoomModeS(self, mode, modeText):
        if self._isDAAPIInited():
            return self.flashObject.as_setZoomMode(mode, modeText)

    def as_setMapDimensionsS(self, widthPx, heightPx):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapDimensions(widthPx, heightPx)

    def as_updateSectorStateStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSectorStateStats(data)

    def as_setMapShortcutKeyCodeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapShortcutKeyCode(value)
