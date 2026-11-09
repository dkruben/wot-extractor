# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/last_update_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/last_update_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.last_update_tooltip_model import LastUpdateTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class LastUpdateTooltip(ViewImpl):
    __slots__ = ()
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.comp7.mono.lobby.tooltips.last_update_tooltip())
        settings.model = LastUpdateTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(LastUpdateTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LastUpdateTooltip, self).getViewModel()

    def _onLoading(self, description, updateTime=None, *args, **kwargs):
        super(LastUpdateTooltip, self)._onLoading(*args, **kwargs)
        self.viewModel.setDescription(description)
        self.viewModel.setLeaderboardUpdateTimestamp(updateTime or 0)
