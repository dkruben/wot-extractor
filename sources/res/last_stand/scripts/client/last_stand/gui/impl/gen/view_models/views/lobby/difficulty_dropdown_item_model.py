# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/difficulty_dropdown_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/difficulty_dropdown_item_model.py
from frameworks.wulf import ViewModel

class DifficultyDropdownItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DifficultyDropdownItemModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getShowWarningIcon(self):
        return self._getBool(1)

    def setShowWarningIcon(self, value):
        self._setBool(1, value)

    def getLabel(self):
        return self._getString(2)

    def setLabel(self, value):
        self._setString(2, value)

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(DifficultyDropdownItemModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addBoolProperty('showWarningIcon', False)
        self._addStringProperty('label', '')
        self._addBoolProperty('isDisabled', False)
