# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/empty_skill_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/empty_skill_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.empty_skill_tooltip_view_model import EmptySkillTooltipViewModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setSkillProgressionModel
from gui.impl.pub import ViewImpl

class EmptySkillTooltip(ViewImpl):
    __slots__ = ('_tankman', '_skillIndex')

    def __init__(self, tankman, skillIndex):
        self._tankman = tankman
        self._skillIndex = skillIndex
        settings = ViewSettings(R.views.lobby.crew.tooltips.EmptySkillTooltip(), model=EmptySkillTooltipViewModel())
        super(EmptySkillTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(EmptySkillTooltip, self).getViewModel()

    def _onLoading(self):
        isZero = self._skillIndex < self._tankman.freeSkillsCount
        with self.viewModel.transaction() as vm:
            vm.setIsZeroSkill(isZero)
            setSkillProgressionModel(vm=vm.skillProgression, tankman=self._tankman, skillIndex=self._skillIndex, isZero=isZero)
