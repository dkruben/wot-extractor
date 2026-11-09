# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/TabScreenMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TabScreenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TabScreenMeta(BaseDAAPIComponent):

    def onSelectQuest(self, questID):
        self._printOverrideError('onSelectQuest')

    def onStatsTableVisibiltyToggled(self, isVisible):
        self._printOverrideError('onStatsTableVisibiltyToggled')

    def as_questProgressPerformS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_questProgressPerform(data)

    def as_updateProgressTrackingS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressTracking(data)

    def as_setActiveTabS(self, tabIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setActiveTab(tabIndex)

    def as_resetActiveTabS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetActiveTab()

    def as_updateTabsS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTabs(dataProvider)
