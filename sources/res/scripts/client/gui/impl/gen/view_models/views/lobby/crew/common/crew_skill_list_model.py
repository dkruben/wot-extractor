# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/crew_skill_list_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/crew_skill_list_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_model import CrewSkillModel

class CrewSkillListModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewSkillListModel, self).__init__(properties=properties, commands=commands)

    def getMajorSkills(self):
        return self._getArray(0)

    def setMajorSkills(self, value):
        self._setArray(0, value)

    @staticmethod
    def getMajorSkillsType():
        return CrewSkillModel

    def getBonusSkills(self):
        return self._getArray(1)

    def setBonusSkills(self, value):
        self._setArray(1, value)

    @staticmethod
    def getBonusSkillsType():
        return CrewSkillModel

    def getSkillsEfficiency(self):
        return self._getReal(2)

    def setSkillsEfficiency(self, value):
        self._setReal(2, value)

    def _initialize(self):
        super(CrewSkillListModel, self)._initialize()
        self._addArrayProperty('majorSkills', Array())
        self._addArrayProperty('bonusSkills', Array())
        self._addRealProperty('skillsEfficiency', 0.0)
