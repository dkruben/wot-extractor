# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_reserves/disabled_category.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_reserves/disabled_category.py
from enum import Enum
from frameworks.wulf import ViewModel

class CategoryType(Enum):
    PERSONAL = 'personal'
    CLAN = 'clan'
    EVENT = 'event'


class DisabledCategory(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DisabledCategory, self).__init__(properties=properties, commands=commands)

    def getCategoryType(self):
        return CategoryType(self._getString(0))

    def setCategoryType(self, value):
        self._setString(0, value.value)

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(DisabledCategory, self)._initialize()
        self._addStringProperty('categoryType')
        self._addBoolProperty('isDisabled', False)
