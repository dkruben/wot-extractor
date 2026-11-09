# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/compare_skills_panel_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/compare_skills_panel_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel

class CompareSkillsPanelViewModel(ViewModel):
    __slots__ = ('onClick', 'onReset')

    def __init__(self, properties=1, commands=2):
        super(CompareSkillsPanelViewModel, self).__init__(properties=properties, commands=commands)

    def getSkills(self):
        return self._getArray(0)

    def setSkills(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSkillsType():
        return SkillSimpleModel

    def _initialize(self):
        super(CompareSkillsPanelViewModel, self)._initialize()
        self._addArrayProperty('skills', Array())
        self.onClick = self._addCommand('onClick')
        self.onReset = self._addCommand('onReset')
