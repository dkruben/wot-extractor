# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/collection/collection_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/collection_model.py
from frameworks.wulf import ViewModel

class CollectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(CollectionModel, self).__init__(properties=properties, commands=commands)

    def getCollectionId(self):
        return self._getNumber(0)

    def setCollectionId(self, value):
        self._setNumber(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)

    def getIsNew(self):
        return self._getBool(3)

    def setIsNew(self, value):
        self._setBool(3, value)

    def getCompletionWasShown(self):
        return self._getBool(4)

    def setCompletionWasShown(self, value):
        self._setBool(4, value)

    def getItemCount(self):
        return self._getNumber(5)

    def setItemCount(self, value):
        self._setNumber(5, value)

    def getMaxCount(self):
        return self._getNumber(6)

    def setMaxCount(self, value):
        self._setNumber(6, value)

    def getYear(self):
        return self._getNumber(7)

    def setYear(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(CollectionModel, self)._initialize()
        self._addNumberProperty('collectionId', 0)
        self._addStringProperty('name', '')
        self._addBoolProperty('isActive', False)
        self._addBoolProperty('isNew', False)
        self._addBoolProperty('completionWasShown', False)
        self._addNumberProperty('itemCount', 0)
        self._addNumberProperty('maxCount', 0)
        self._addNumberProperty('year', 0)
