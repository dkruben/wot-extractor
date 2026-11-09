# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PlayersPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PlayersPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.base_stats import StatsBase

class PlayersPanelMeta(StatsBase):

    def tryToSetPanelModeByMouse(self, panelMode):
        self._printOverrideError('tryToSetPanelModeByMouse')

    def switchToOtherPlayer(self, vehicleID):
        self._printOverrideError('switchToOtherPlayer')

    def as_setPanelModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelMode(value)

    def as_setChatCommandsVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommandsVisibility(value)

    def as_setPlayerHPS(self, isAlly, index, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerHP(isAlly, index, percent)

    def as_setOverrideExInfoS(self, exOverrideInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setOverrideExInfo(exOverrideInfo)

    def as_setPanelHPBarVisibilityStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelHPBarVisibilityState(value)
