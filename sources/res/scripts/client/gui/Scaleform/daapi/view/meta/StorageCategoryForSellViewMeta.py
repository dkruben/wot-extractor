# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryForSellViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryForSellViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.category_view import InventoryCategoryView

class StorageCategoryForSellViewMeta(InventoryCategoryView):

    def navigateToStore(self):
        self._printOverrideError('navigateToStore')

    def selectItem(self, itemId, isSelected):
        self._printOverrideError('selectItem')

    def selectAll(self, isSelected):
        self._printOverrideError('selectAll')

    def sellItem(self, itemId):
        self._printOverrideError('sellItem')

    def sellAll(self):
        self._printOverrideError('sellAll')

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
