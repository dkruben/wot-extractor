# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/skill_select_row_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/skill_select_row_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.skill_select_item_model import SkillSelectItemModel

class SkillSelectRowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SkillSelectRowModel, self).__init__(properties=properties, commands=commands)

    def getSkills(self):
        return self._getArray(0)

    def setSkills(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSkillsType():
        return SkillSelectItemModel

    def getCommonSkills(self):
        return self._getArray(1)

    def setCommonSkills(self, value):
        self._setArray(1, value)

    @staticmethod
    def getCommonSkillsType():
        return SkillSelectItemModel

    def getRole(self):
        return self._getString(2)

    def setRole(self, value):
        self._setString(2, value)

    def getPossibleMaxSelected(self):
        return self._getNumber(3)

    def setPossibleMaxSelected(self, value):
        self._setNumber(3, value)

    def getSelectedAmount(self):
        return self._getNumber(4)

    def setSelectedAmount(self, value):
        self._setNumber(4, value)

    def getTankmanIdx(self):
        return self._getNumber(5)

    def setTankmanIdx(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(SkillSelectRowModel, self)._initialize()
        self._addArrayProperty('skills', Array())
        self._addArrayProperty('commonSkills', Array())
        self._addStringProperty('role', '')
        self._addNumberProperty('possibleMaxSelected', 0)
        self._addNumberProperty('selectedAmount', 0)
        self._addNumberProperty('tankmanIdx', -1)
