# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/common/stat_column_settings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/common/stat_column_settings_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel

class ColumnEnum(Enum):
    KILLS = 'kills'
    DAMAGE = 'damage'
    ASSIST = 'assist'
    BLOCKED = 'blocked'
    PLACE = 'place'
    KEYS = 'keys'


class StatColumnSettingsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(StatColumnSettingsModel, self).__init__(properties=properties, commands=commands)

    def getVisibleColumns(self):
        return self._getArray(0)

    def setVisibleColumns(self, value):
        self._setArray(0, value)

    @staticmethod
    def getVisibleColumnsType():
        return ColumnEnum

    def _initialize(self):
        super(StatColumnSettingsModel, self)._initialize()
        self._addArrayProperty('visibleColumns', Array())
