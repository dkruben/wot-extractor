# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/collection/item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/item_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ItemState(Enum):
    NEW = 'new'
    RECEIVED = 'received'
    UNRECEIVED = 'unreceived'


class ItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ItemModel, self).__init__(properties=properties, commands=commands)

    def getItemId(self):
        return self._getNumber(0)

    def setItemId(self, value):
        self._setNumber(0, value)

    def getState(self):
        return ItemState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)

    def getReceivedImagePath(self):
        return self._getString(2)

    def setReceivedImagePath(self, value):
        self._setString(2, value)

    def getUnreceivedImagePath(self):
        return self._getString(3)

    def setUnreceivedImagePath(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(ItemModel, self)._initialize()
        self._addNumberProperty('itemId', 0)
        self._addStringProperty('state')
        self._addStringProperty('receivedImagePath', '')
        self._addStringProperty('unreceivedImagePath', '')
