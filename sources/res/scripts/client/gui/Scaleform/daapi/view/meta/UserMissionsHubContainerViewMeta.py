# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/UserMissionsHubContainerViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/UserMissionsHubContainerViewMeta.py
from gui.Scaleform.framework.entities.View import View

class UserMissionsHubContainerViewMeta(View):

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def onClose(self):
        self._printOverrideError('onClose')

    def as_showFilterCounterS(self, countText, isFilterApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterCounter(countText, isFilterApplied)

    def as_blinkFilterCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkFilterCounter()

    def as_updateCommonMissionsTabVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommonMissionsTabVisibility(isVisible)

    def as_updateCommonMissionsTabPositionS(self, posY, maxHeight):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommonMissionsTabPosition(posY, maxHeight)

    def as_setBackgroundS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(source)
