# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/dismissed_toggle_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/dismissed_toggle_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.dismissed_toggle_tooltip_model import DismissedToggleTooltipModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanRestoreInfo
from gui.impl.pub import ViewImpl

class DismissedToggleTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.crew.tooltips.DismissedToggleTooltip(), args=args, kwargs=kwargs)
        settings.model = DismissedToggleTooltipModel()
        super(DismissedToggleTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(DismissedToggleTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(DismissedToggleTooltip, self)._onLoading(*args, **kwargs)
        self._fillModel()

    def _fillModel(self):
        with self.viewModel.transaction() as vm:
            setTankmanRestoreInfo(vm)
