# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/entities/DAAPIDataProvider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/DAAPIDataProvider.py
from __future__ import absolute_import
from future.utils import lmap
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule
from gui.shared.utils import sortByFields

class DAAPIDataProvider(BaseDAAPIModule):

    def __init__(self):
        super(DAAPIDataProvider, self).__init__()
        self._itemWrapper = lambda x: x

    def _dispose(self):
        super(DAAPIDataProvider, self)._dispose()
        self.clearItemWrapper()

    @property
    def collection(self):
        raise NotImplementedError

    def buildList(self, *args):
        raise NotImplementedError

    def emptyItem(self):
        return NotImplementedError

    def setItemWrapper(self, wrapper):
        self._itemWrapper = wrapper

    def clearItemWrapper(self):
        self._itemWrapper = lambda x: x

    def lengthHandler(self):
        return self.pyLength()

    def requestItemAtHandler(self, idx):
        return self.pyRequestItemAt(idx)

    def requestItemRangeHandler(self, startIndex, endIndex):
        return self.pyRequestItemRange(startIndex, endIndex)

    def refresh(self):
        if self.flashObject is not None:
            self.flashObject.invalidate(self.pyLength())
        return

    def pyLength(self):
        return len(self.collection)

    def pyRequestItemAt(self, idx):
        if -1 < idx < self.pyLength():
            return self._itemWrapper(self.collection[int(idx)])
        else:
            return

    def pyRequestItemRange(self, startIndex, endIndex):
        return lmap(self._itemWrapper, self.collection[int(startIndex):int(endIndex) + 1])


class SortableDAAPIDataProvider(DAAPIDataProvider):

    def __init__(self):
        super(SortableDAAPIDataProvider, self).__init__()
        self._sort = ()

    @property
    def sortedCollection(self):
        return sortByFields(self._sort, self.collection)

    def sortOnHandler(self, fieldName, options):
        return self.pySortOn(fieldName, options)

    def getSelectedIdxHandler(self):
        return self.pyGetSelectedIdx()

    def pyRequestItemAt(self, idx):
        if -1 < idx < self.pyLength():
            return self._itemWrapper(self.sortedCollection[int(idx)])
        else:
            return

    def pyRequestItemRange(self, startIndex, endIndex):
        return lmap(self._itemWrapper, self.sortedCollection[int(startIndex):int(endIndex) + 1])

    def pySortOn(self, fields, order):
        self._sort = tuple(zip(fields, order))

    def pyGetSelectedIdx(self):
        return -1


class ListDAAPIDataProvider(DAAPIDataProvider):

    def __init__(self):
        super(ListDAAPIDataProvider, self).__init__()
        self._sort = ()

    @property
    def sortedCollection(self):
        return sortByFields(self._sort, self.collection)

    def sortOnHandler(self, fieldName, options):
        return self.pySortOn(fieldName, options)

    def getSelectedIdxHandler(self):
        return self.pyGetSelectedIdx()

    def pyRequestItemAt(self, idx):
        if -1 < idx < self.pyLength():
            return self._itemWrapper(self.sortedCollection[int(idx)])
        else:
            return

    def pyRequestItemRange(self, startIndex, endIndex):
        return lmap(self._itemWrapper, self.sortedCollection[int(startIndex):int(endIndex) + 1])

    def pySortOn(self, fields, order):
        self._sort = tuple(zip(fields, order))

    def pyGetSelectedIdx(self):
        return -1

    def refreshRandomItems(self, indexes, items):
        self.flashObject.invalidateItems(indexes, items)

    def refreshSingleItem(self, index, item):
        self.flashObject.invalidateItem(index, item)
