# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/tooltips/selected_rewards_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/tooltips/selected_rewards_tooltip_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_category_model import SelectedRewardsTooltipCategoryModel

class SelectedRewardsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SelectedRewardsTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getCategories(self):
        return self._getArray(0)

    def setCategories(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCategoriesType():
        return SelectedRewardsTooltipCategoryModel

    def getTotalSelected(self):
        return self._getNumber(1)

    def setTotalSelected(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(SelectedRewardsTooltipViewModel, self)._initialize()
        self._addArrayProperty('categories', Array())
        self._addNumberProperty('totalSelected', 0)
