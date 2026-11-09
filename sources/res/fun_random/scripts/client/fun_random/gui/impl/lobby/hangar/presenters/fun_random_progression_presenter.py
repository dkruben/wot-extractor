# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_progression_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_progression_presenter.py
from __future__ import absolute_import
import typing
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_progression_entry_point_model import FunRandomProgressionEntryPointModel
from fun_random.gui.impl.lobby.tooltips.fun_random_progression_tooltip_view import FunRandomProgressionTooltipView
from fun_random.gui.impl.lobby.common.fun_view_helpers import defineProgressionStatus, packProgressionState, packProgressionActiveStage, packInfiniteProgressionState, packInfiniteProgressionStage
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from fun_random.gui.impl.lobby.hangar.controllers.fun_random_overlap_controller import FunRandomOverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin
if typing.TYPE_CHECKING:
    from frameworks.wulf import View, ViewEvent

class FunRandomProgressionPresenter(TooltipPositionerMixin, FunRandomOverlapCtrlMixin, ViewComponent[FunRandomProgressionEntryPointModel], FunProgressionWatcher):

    def __init__(self):
        super(FunRandomProgressionPresenter, self).__init__(model=FunRandomProgressionEntryPointModel)

    @property
    def viewModel(self):
        return super(FunRandomProgressionPresenter, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.fun_random.mono.lobby.tooltips.progression_tooltip():
            return FunRandomProgressionTooltipView()
        return super(FunRandomProgressionPresenter, self).createToolTipContent(event, contentID)

    def setDisabledProgression(self):
        self.viewModel.progressionState.setStatus(defineProgressionStatus(None))
        return

    @hasActiveProgression()
    def showActiveProgressionPage(self, *_):
        super(FunRandomProgressionPresenter, self).showActiveProgressionPage()

    def _onLoading(self, *args, **kwargs):
        self.initOverlapCtrl()
        super(FunRandomProgressionPresenter, self)._onLoading(*args, **kwargs)
        self.startProgressionListening(self._updateViewModel)
        self._updateViewModel()

    def _finalize(self):
        self.stopProgressionListening(self._updateViewModel)
        super(FunRandomProgressionPresenter, self)._finalize()

    def _getEvents(self):
        return super(FunRandomProgressionPresenter, self)._getEvents() + (
         (
          self.viewModel.onShowInfo, self.showActiveProgressionPage),)

    @hasActiveProgression(abortAction='setDisabledProgression')
    def _rawUpdate(self):
        super(FunRandomProgressionPresenter, self)._rawUpdate()
        with self.viewModel.transaction() as model:
            progression = self.getActiveProgression()
            model.progressionState.setStatus(defineProgressionStatus(progression))
            if progression.isInUnlimitedProgression:
                packInfiniteProgressionState(progression, model.progressionState)
                packInfiniteProgressionStage(progression, model.currentProgressionStage)
            else:
                packProgressionState(progression, model.progressionState)
                packProgressionActiveStage(progression, model.currentProgressionStage)

    @hasActiveProgression(abortAction='setDisabledProgression')
    def _updateViewModel(self, *_):
        self.queueUpdate()
