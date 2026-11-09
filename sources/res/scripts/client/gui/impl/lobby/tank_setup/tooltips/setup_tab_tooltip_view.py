# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/tooltips/setup_tab_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/tooltips/setup_tab_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.setup_tab_tooltip_view_model import SetupTabTooltipViewModel
from gui.impl.pub import ViewImpl

class SetupTabTooltipView(ViewImpl):

    def __init__(self, name):
        settings = ViewSettings(R.views.lobby.tanksetup.tooltips.SetupTabTooltipView())
        settings.model = SetupTabTooltipViewModel()
        settings.args = (name,)
        super(SetupTabTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SetupTabTooltipView, self).getViewModel()

    def _onLoading(self, name, *args, **kwargs):
        super(SetupTabTooltipView, self)._onLoading(*args, **kwargs)
        self.viewModel.setName(name)
