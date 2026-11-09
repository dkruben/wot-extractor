# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/research_item_display_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/research_item_display_model.py
from frameworks.wulf import Array, ViewModel

class ResearchItemDisplayModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ResearchItemDisplayModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getRenderer(self):
        return self._getString(2)

    def setRenderer(self, value):
        self._setString(2, value)

    def getPath(self):
        return self._getArray(3)

    def setPath(self, value):
        self._setArray(3, value)

    @staticmethod
    def getPathType():
        return int

    def _initialize(self):
        super(ResearchItemDisplayModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addNumberProperty('level', -1)
        self._addStringProperty('renderer', '')
        self._addArrayProperty('path', Array())
