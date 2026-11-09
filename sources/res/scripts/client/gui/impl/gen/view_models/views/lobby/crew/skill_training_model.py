# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/skill_training_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/skill_training_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_extended_model import SkillExtendedModel

class SkillTrainingModel(SkillExtendedModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(SkillTrainingModel, self).__init__(properties=properties, commands=commands)

    def getIsSelected(self):
        return self._getBool(9)

    def setIsSelected(self, value):
        self._setBool(9, value)

    def getIsLearned(self):
        return self._getBool(10)

    def setIsLearned(self, value):
        self._setBool(10, value)

    def getPopularityList(self):
        return self._getArray(11)

    def setPopularityList(self, value):
        self._setArray(11, value)

    @staticmethod
    def getPopularityListType():
        return int

    def _initialize(self):
        super(SkillTrainingModel, self)._initialize()
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isLearned', False)
        self._addArrayProperty('popularityList', Array())
