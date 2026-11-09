# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BaseStorageCategoryViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseStorageCategoryViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseStorageCategoryViewMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError('setActiveState')

    def playInfoSound(self):
        self._printOverrideError('playInfoSound')

    def scrolledToBottom(self):
        self._printOverrideError('scrolledToBottom')

    def as_showDummyScreenS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showDummyScreen(show)

    def as_showFilterWarningS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterWarning(data)

    def as_getCardsDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCardsDP()

    def as_scrollToItemS(self, itemIntCD):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToItem(itemIntCD)
