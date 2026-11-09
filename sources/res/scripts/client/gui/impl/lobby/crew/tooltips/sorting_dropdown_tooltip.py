# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/sorting_dropdown_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/sorting_dropdown_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.crew.tooltips import sorting_dropdown_tooltip_model as tt_model
from gui.impl.pub import ViewImpl

class SortingDropdownTooltip(ViewImpl):

    def __init__(self, layoutID, *args, **kwargs):
        settings = ViewSettings(layoutID)
        settings.model = tt_model.SortingDropdownTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(SortingDropdownTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SortingDropdownTooltip, self).getViewModel()

    def _onLoading(self, isWarningShown, isSortingDisabled, *args, **kwargs):
        super(SortingDropdownTooltip, self)._onLoading(*args, **kwargs)
        self.viewModel.setShowSortingSelectionWarning(isWarningShown)
        self.viewModel.setIsSortingDisabled(isSortingDisabled)
