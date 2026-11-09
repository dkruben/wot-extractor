# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/collection/tooltips/collection_item_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/tooltips/collection_item_tooltip_view_model.py
from frameworks.wulf import ViewModel

class CollectionItemTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CollectionItemTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)

    def getIsReceived(self):
        return self._getBool(2)

    def setIsReceived(self, value):
        self._setBool(2, value)

    def getImagePath(self):
        return self._getString(3)

    def setImagePath(self, value):
        self._setString(3, value)

    def getIsDetailed(self):
        return self._getBool(4)

    def setIsDetailed(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(CollectionItemTooltipViewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('description', '')
        self._addBoolProperty('isReceived', False)
        self._addStringProperty('imagePath', '')
        self._addBoolProperty('isDetailed', False)
