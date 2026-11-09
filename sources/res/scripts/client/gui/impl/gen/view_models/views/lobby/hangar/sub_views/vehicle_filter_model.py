# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_filter_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_filter_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel

class RoleSection(Enum):
    LIGHTTANK = 'light_tank'
    MEDIUMTANK = 'medium_tank'
    HEAVYTANK = 'heavy_tank'
    ATSPG = 'at_spg'


class FilterSection(Enum):
    NATIONS = 'nations'
    VEHICLETYPES = 'vehicle_types'
    LEVELS = 'levels'
    SPECIALS = 'specials'
    TEXTSEARCH = 'text_search'
    ROLES = 'roles'
    BATTLEPASS = 'battle_pass'


class VehicleFilterModel(ViewModel):
    __slots__ = ('onSaveFilter', 'onCarouselTypeChange', 'onResetFilter')

    def __init__(self, properties=4, commands=3):
        super(VehicleFilterModel, self).__init__(properties=properties, commands=commands)

    def getFilters(self):
        return self._getString(0)

    def setFilters(self, value):
        self._setString(0, value)

    def getDefaultFilters(self):
        return self._getString(1)

    def setDefaultFilters(self, value):
        self._setString(1, value)

    def getNationsOrder(self):
        return self._getArray(2)

    def setNationsOrder(self, value):
        self._setArray(2, value)

    @staticmethod
    def getNationsOrderType():
        return unicode

    def getCarouselRowCount(self):
        return self._getNumber(3)

    def setCarouselRowCount(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(VehicleFilterModel, self)._initialize()
        self._addStringProperty('filters', '')
        self._addStringProperty('defaultFilters', '{}')
        self._addArrayProperty('nationsOrder', Array())
        self._addNumberProperty('carouselRowCount', 0)
        self.onSaveFilter = self._addCommand('onSaveFilter')
        self.onCarouselTypeChange = self._addCommand('onCarouselTypeChange')
        self.onResetFilter = self._addCommand('onResetFilter')
