# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/list_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/list_model.py
import typing
from frameworks.wulf import Array, ViewModel
T = typing.TypeVar('T')

class ListModel(ViewModel, typing.Generic[T]):
    __slots__ = ('onSelectionChanged', 'onItemClicked')

    def __init__(self, properties=2, commands=2):
        super(ListModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getItemsType():
        return T

    def getSelectedIndices(self):
        return self._getArray(1)

    def setSelectedIndices(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSelectedIndicesType():
        return int

    def _initialize(self):
        super(ListModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self._addArrayProperty('selectedIndices', Array())
        self.onSelectionChanged = self._addCommand('onSelectionChanged')
        self.onItemClicked = self._addCommand('onItemClicked')
