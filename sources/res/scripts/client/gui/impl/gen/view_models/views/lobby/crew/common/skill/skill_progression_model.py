# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_progression_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_progression_model.py
from frameworks.wulf import ViewModel

class SkillProgressionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(SkillProgressionModel, self).__init__(properties=properties, commands=commands)

    def getCurrentXpValue(self):
        return self._getNumber(0)

    def setCurrentXpValue(self, value):
        self._setNumber(0, value)

    def getTotalXpValue(self):
        return self._getNumber(1)

    def setTotalXpValue(self, value):
        self._setNumber(1, value)

    def getSkillProgress(self):
        return self._getNumber(2)

    def setSkillProgress(self, value):
        self._setNumber(2, value)

    def getDiscountValue(self):
        return self._getNumber(3)

    def setDiscountValue(self, value):
        self._setNumber(3, value)

    def getZeroSkillsCount(self):
        return self._getNumber(4)

    def setZeroSkillsCount(self, value):
        self._setNumber(4, value)

    def getIsLocked(self):
        return self._getBool(5)

    def setIsLocked(self, value):
        self._setBool(5, value)

    def getIsMaxSkillLevel(self):
        return self._getBool(6)

    def setIsMaxSkillLevel(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(SkillProgressionModel, self)._initialize()
        self._addNumberProperty('currentXpValue', 0)
        self._addNumberProperty('totalXpValue', 0)
        self._addNumberProperty('skillProgress', 0)
        self._addNumberProperty('discountValue', 0)
        self._addNumberProperty('zeroSkillsCount', 0)
        self._addBoolProperty('isLocked', False)
        self._addBoolProperty('isMaxSkillLevel', False)
