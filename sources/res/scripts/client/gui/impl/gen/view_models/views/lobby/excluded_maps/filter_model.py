# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/excluded_maps/filter_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/excluded_maps/filter_model.py
from frameworks.wulf import ViewModel

class FilterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FilterModel, self).__init__(properties=properties, commands=commands)

    def getFilterName(self):
        return self._getString(0)

    def setFilterName(self, value):
        self._setString(0, value)

    def getFilterId(self):
        return self._getNumber(1)

    def setFilterId(self, value):
        self._setNumber(1, value)

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(FilterModel, self)._initialize()
        self._addStringProperty('filterName', '')
        self._addNumberProperty('filterId', -1)
        self._addBoolProperty('isActive', False)
