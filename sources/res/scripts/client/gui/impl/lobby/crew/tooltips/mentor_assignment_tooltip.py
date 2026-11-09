# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/mentor_assignment_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/mentor_assignment_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.mentor_assignment_tooltip_model import MentorAssignmentTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class MentorAssignmentTooltip(ViewImpl):
    __slots__ = ('sourceTmanID', 'targetTmanID')
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, sourceTmanID, targetTmanID, *args, **kwargs):
        self.sourceTmanID = sourceTmanID
        self.targetTmanID = targetTmanID
        settings = ViewSettings(R.views.lobby.crew.tooltips.MentorAssignmentTooltip(), args=args, kwargs=kwargs)
        settings.model = MentorAssignmentTooltipModel()
        super(MentorAssignmentTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MentorAssignmentTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(MentorAssignmentTooltip, self)._onLoading(*args, **kwargs)
        self._fillModel()

    def _fillModel(self):
        sourceTman = self._itemsCache.items.getTankman(self.sourceTmanID)
        targetTman = self._itemsCache.items.getTankman(self.targetTmanID)
        with self.viewModel.transaction() as vm:
            vm.setFullName(sourceTman.getFullUserNameWithSkin())
            vm.setHasFreeSkills(targetTman.freeSkillsCount > 0)
