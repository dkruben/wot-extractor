# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/MissionsPageMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsPageMeta.py
from gui.Scaleform.framework.entities.View import View

class MissionsPageMeta(View):

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def onTabSelected(self, alias, prefix):
        self._printOverrideError('onTabSelected')

    def onClose(self):
        self._printOverrideError('onClose')

    def as_setTabsDataProviderS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsDataProvider(dataProvider)

    def as_showFilterS(self, visible, topShadowVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilter(visible, topShadowVisible)

    def as_showFilterCounterS(self, countText, isFilterApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterCounter(countText, isFilterApplied)

    def as_blinkFilterCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkFilterCounter()

    def as_setTabsCounterDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsCounterData(data)

    def as_showBattleMattersAnimationS(self, animPath, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showBattleMattersAnimation(animPath, data)
