# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/seniority_awards/tooltip/seniority_awards_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/seniority_awards/tooltip/seniority_awards_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_tooltip_model import SeniorityAwardsTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import ISeniorityAwardsController

class SeniorityAwardsTooltip(ViewImpl):
    __slots__ = ()
    __seniorityAwardsCtrl = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.seniority_awards.tooltips.seniority_tooltip())
        settings.model = SeniorityAwardsTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(SeniorityAwardsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SeniorityAwardsTooltip, self).getViewModel()

    def _onLoading(self, category, maxCategory, years):
        categories = list(self.__seniorityAwardsCtrl.categories.items())
        categories = sorted(categories, key=(lambda item: item[1][0]))
        with self.viewModel.transaction() as vm:
            vm.setCategory(category)
            vm.setMaxCategory(maxCategory)
            vm.setYears(years)
            for ctgId, _ in categories:
                vm.getCategories().addString(ctgId.lower())
