# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/tankman_skills_group_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/tankman_skills_group_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skill_model import TankmanSkillModel

class TankmanSkillsGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TankmanSkillsGroupModel, self).__init__(properties=properties, commands=commands)

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)

    def getDirectiveId(self):
        return self._getNumber(1)

    def setDirectiveId(self, value):
        self._setNumber(1, value)

    def getDirectiveName(self):
        return self._getString(2)

    def setDirectiveName(self, value):
        self._setString(2, value)

    def getSelectedSkillsCount(self):
        return self._getNumber(3)

    def setSelectedSkillsCount(self, value):
        self._setNumber(3, value)

    def getSkills(self):
        return self._getArray(4)

    def setSkills(self, value):
        self._setArray(4, value)

    @staticmethod
    def getSkillsType():
        return TankmanSkillModel

    def _initialize(self):
        super(TankmanSkillsGroupModel, self)._initialize()
        self._addStringProperty('role', '')
        self._addNumberProperty('directiveId', 0)
        self._addStringProperty('directiveName', '')
        self._addNumberProperty('selectedSkillsCount', 0)
        self._addArrayProperty('skills', Array())
