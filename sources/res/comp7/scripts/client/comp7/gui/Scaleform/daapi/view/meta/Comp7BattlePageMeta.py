# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/meta/Comp7BattlePageMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/meta/Comp7BattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class Comp7BattlePageMeta(ClassicPage):

    def showHelp(self):
        self._printOverrideError('showHelp')

    def moveSpace(self, x, y, delta):
        self._printOverrideError('moveSpace')

    def notifyCursorOver3dScene(self, isOver3dScene):
        self._printOverrideError('notifyCursorOver3dScene')

    def notifyCursorDragging(self, isDragging):
        self._printOverrideError('notifyCursorDragging')

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)

    def as_onVehicleSelectionConfirmedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onVehicleSelectionConfirmed()

    def as_onBattleStartedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onBattleStarted()

    def as_onPrebattleInputStateLockedS(self, isStateLocked):
        if self._isDAAPIInited():
            return self.flashObject.as_onPrebattleInputStateLocked(isStateLocked)
