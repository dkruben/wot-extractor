# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/filters_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/filters_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.sub_filter_model import SubFilterModel

class FiltersModel(ViewModel):
    __slots__ = ('onFilterChanged', 'onFilterReset')

    def __init__(self, properties=4, commands=2):
        super(FiltersModel, self).__init__(properties=properties, commands=commands)

    def getSelectedFilterCount(self):
        return self._getNumber(0)

    def setSelectedFilterCount(self, value):
        self._setNumber(0, value)

    def getTotalFilterCount(self):
        return self._getNumber(1)

    def setTotalFilterCount(self, value):
        self._setNumber(1, value)

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)

    def getFilters(self):
        return self._getArray(3)

    def setFilters(self, value):
        self._setArray(3, value)

    @staticmethod
    def getFiltersType():
        return SubFilterModel

    def _initialize(self):
        super(FiltersModel, self)._initialize()
        self._addNumberProperty('selectedFilterCount', 0)
        self._addNumberProperty('totalFilterCount', 0)
        self._addBoolProperty('isEnabled', False)
        self._addArrayProperty('filters', Array())
        self.onFilterChanged = self._addCommand('onFilterChanged')
        self.onFilterReset = self._addCommand('onFilterReset')
