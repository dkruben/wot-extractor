# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/ListPaginator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/ListPaginator.py
from __future__ import absolute_import
import weakref
from past.utils import old_div
import Event

class ListPaginator(object):

    def __init__(self, requester, offset=None, count=20):
        super(ListPaginator, self).__init__()
        self._eManager = Event.EventManager()
        self.onListUpdated = Event.Event(self._eManager)
        if offset is not None:
            self.__initialOffset = offset
        else:
            self.__initialOffset = old_div(-count, 2)
        self._offset = self.__initialOffset
        self._prevOffset = self._offset
        self._count = count
        self._selectedID = None
        self._requester = weakref.proxy(requester)
        return

    def init(self):
        pass

    def fini(self):
        self._eManager.clear()

    def canMoveLeft(self):
        return True

    def canMoveRight(self):
        return True

    def right(self):
        self._selectedID = None
        self._prevOffset = self._offset
        self._offset += self._count
        self._request()
        return

    def left(self):
        self._selectedID = None
        self._prevOffset = self._offset
        self._offset -= self._count
        self._request()
        return

    def reset(self):
        self._selectedID = None
        self._offset = self.__initialOffset
        self._prevOffset = self._offset
        self._request(isReset=True)
        return

    def getInitialOffset(self):
        return self.__initialOffset

    def revertOffset(self):
        self._offset = self._prevOffset

    def refresh(self, *args, **kwargs):
        self._request()

    def setSelectedID(self, selectedID):
        self._selectedID = selectedID

    def getSelectedID(self):
        return self._selectedID

    def _request(self, isReset=False):
        raise NotImplementedError
