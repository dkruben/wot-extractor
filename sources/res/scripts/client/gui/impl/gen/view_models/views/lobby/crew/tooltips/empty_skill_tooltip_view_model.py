# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/empty_skill_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/empty_skill_tooltip_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_progression_model import SkillProgressionModel

class EmptySkillTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EmptySkillTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def skillProgression(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillProgressionType():
        return SkillProgressionModel

    def getIsZeroSkill(self):
        return self._getBool(1)

    def setIsZeroSkill(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(EmptySkillTooltipViewModel, self)._initialize()
        self._addViewModelProperty('skillProgression', SkillProgressionModel())
        self._addBoolProperty('isZeroSkill', False)
