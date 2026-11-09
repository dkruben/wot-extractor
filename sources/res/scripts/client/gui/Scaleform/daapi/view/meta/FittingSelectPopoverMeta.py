# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):

    def setVehicleModule(self, newId, oldId, isRemove):
        self._printOverrideError('setVehicleModule')

    def upgradeVehicleModule(self, moduleId):
        self._printOverrideError('upgradeVehicleModule')

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def setAutoRearm(self, autoRearm):
        self._printOverrideError('setAutoRearm')

    def buyVehicleModule(self, moduleId):
        self._printOverrideError('buyVehicleModule')

    def setCurrentTab(self, tabIndex):
        self._printOverrideError('setCurrentTab')

    def listOverlayClosed(self):
        self._printOverrideError('listOverlayClosed')

    def onManageBattleAbilitiesClicked(self):
        self._printOverrideError('onManageBattleAbilitiesClicked')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
