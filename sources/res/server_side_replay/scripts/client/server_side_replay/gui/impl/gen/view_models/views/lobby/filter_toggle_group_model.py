# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/filter_toggle_group_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/filter_toggle_group_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_button_model import FilterToggleButtonModel

class ToggleGroupType(Enum):
    DEFAULT = 'default'
    NATION = 'nation'
    LOCATION = 'location'
    TANKMANROLE = 'tankmanRole'
    TANKMANKIND = 'tankmanKind'
    VEHICLEGRADE = 'vehicleGrade'
    VEHICLETIER = 'vehicleTier'
    VEHICLETYPE = 'vehicleType'
    PERSONALDATATYPE = 'personalDataType'
    VEHICLECD = 'vehicle'


class FilterToggleGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FilterToggleGroupModel, self).__init__(properties=properties, commands=commands)

    def getLabel(self):
        return self._getResource(0)

    def setLabel(self, value):
        self._setResource(0, value)

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)

    def getType(self):
        return ToggleGroupType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)

    def getHasDiscount(self):
        return self._getBool(3)

    def setHasDiscount(self, value):
        self._setBool(3, value)

    def getFilters(self):
        return self._getArray(4)

    def setFilters(self, value):
        self._setArray(4, value)

    @staticmethod
    def getFiltersType():
        return FilterToggleButtonModel

    def _initialize(self):
        super(FilterToggleGroupModel, self)._initialize()
        self._addResourceProperty('label', R.invalid())
        self._addStringProperty('id', '')
        self._addStringProperty('type')
        self._addBoolProperty('hasDiscount', False)
        self._addArrayProperty('filters', Array())
