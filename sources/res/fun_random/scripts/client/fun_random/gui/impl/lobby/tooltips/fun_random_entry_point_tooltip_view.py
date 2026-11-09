# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_entry_point_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_entry_point_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from fun_random.gui.feature.fun_constants import FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_entry_point_tooltip_view_model import FunRandomEntryPointTooltipViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import packPerformanceAlertInfo, getFunRandomEventState
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from helpers import time_utils

class FunRandomEntryPointTooltipView(ViewImpl, FunAssetPacksMixin, FunSubModesWatcher):

    def __init__(self):
        settings = ViewSettings(R.views.fun_random.mono.lobby.tooltips.entry_point_tooltip(), model=FunRandomEntryPointTooltipViewModel())
        super(FunRandomEntryPointTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FunRandomEntryPointTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as model:
            status = self.getSubModesStatus()
            model.setAssetsPointer(self.getModeAssetsPointer())
            model.setModeState(getFunRandomEventState(status))
            endTime = status.endTime
            leftTime = status.primeDelta if status.state == FunSubModesState.NOT_AVAILABLE else time_utils.getTimeDeltaFromNowInLocal(endTime)
            model.setStartTime(status.rightBorder)
            model.setLeftTime(leftTime)
            model.setEndTime(endTime)
            packPerformanceAlertInfo(model.performance, self._funRandomCtrl.subModesInfo.getPerformanceAlertGroup())
