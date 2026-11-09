# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BadgesPageMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BadgesPageMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class BadgesPageMeta(WrapperViewMeta):

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onSelectBadge(self, badgeID):
        self._printOverrideError('onSelectBadge')

    def onDeselectBadge(self):
        self._printOverrideError('onDeselectBadge')

    def onSelectSuffixBadge(self, badgeID):
        self._printOverrideError('onSelectSuffixBadge')

    def onDeselectSuffixBadge(self):
        self._printOverrideError('onDeselectSuffixBadge')

    def onDummyButtonPress(self):
        self._printOverrideError('onDummyButtonPress')

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setReceivedBadgesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivedBadges(data)

    def as_setNotReceivedBadgesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotReceivedBadges(data)

    def as_setSelectedBadgeS(self, data, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedBadge(data, selected)

    def as_setBadgeSuffixS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBadgeSuffix(data)
