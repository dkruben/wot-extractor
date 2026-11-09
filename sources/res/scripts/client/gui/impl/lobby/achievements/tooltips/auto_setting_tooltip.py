# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/achievements/tooltips/auto_setting_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/achievements/tooltips/auto_setting_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.auto_setting_tooltip_model import AutoSettingTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class AutoSettingTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.achievements.tooltips.AutoSettingTooltip())
        settings.model = AutoSettingTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(AutoSettingTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(AutoSettingTooltip, self).getViewModel()

    def _onLoading(self, isSwitchedOn):
        with self.viewModel.transaction() as model:
            model.setIsSwitchedOn(isSwitchedOn)
