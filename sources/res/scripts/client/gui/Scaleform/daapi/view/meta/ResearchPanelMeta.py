# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ResearchPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ResearchPanelMeta(BaseDAAPIComponent):

    def goToResearch(self):
        self._printOverrideError('goToResearch')

    def goToPostProgression(self):
        self._printOverrideError('goToPostProgression')

    def addVehToCompare(self):
        self._printOverrideError('addVehToCompare')

    def as_updateCurrentVehicleS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCurrentVehicle(data)

    def as_setEarnedXPS(self, earnedXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setEarnedXP(earnedXP)

    def as_setEliteS(self, isElite):
        if self._isDAAPIInited():
            return self.flashObject.as_setElite(isElite)

    def as_setIGRLabelS(self, visible, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIGRLabel(visible, value)

    def as_actionIGRDaysLeftS(self, visible, value):
        if self._isDAAPIInited():
            return self.flashObject.as_actionIGRDaysLeft(visible, value)

    def as_setNavigationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setNavigationEnabled(value)

    def as_setModuleUpdateAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setModuleUpdateAvailable(value)
