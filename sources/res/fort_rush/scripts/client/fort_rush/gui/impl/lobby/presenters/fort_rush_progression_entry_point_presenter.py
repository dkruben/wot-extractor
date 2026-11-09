# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_progression_entry_point_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_progression_entry_point_presenter.py
from __future__ import absolute_import
from fort_rush.account_helpers.account_settings import getLastSeenProgressionPoints
from fort_rush.gui.impl.gen.view_models.views.lobby.hangar_progression_widget_view_model import HangarProgressionWidgetViewModel
from fort_rush.gui.impl.lobby.tooltips.fort_rush_progression_tooltip import FortRushProgressionWidgetTooltipView
from fort_rush.gui.shared.event_dispatcher import showProgressionView
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from gui.impl.gen import R
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent
from gui.shared.items_cache import CACHE_SYNC_REASON
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from skeletons.gui.server_events import IEventsCache

class FortRushProgressionEntryPointPresenter(UserMissionChildPresenter, TooltipPositionerMixin, ViewComponent[HangarProgressionWidgetViewModel]):
    __ctrl = dependency.descriptor(IFortRushBattleController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, *args, **kwargs):
        super(FortRushProgressionEntryPointPresenter, self).__init__(layoutID=R.aliases.fort_rush.shared.Progression(), model=HangarProgressionWidgetViewModel)

    @property
    def viewModel(self):
        return self.getViewModel()

    @property
    def hasDeferModelUpdate(self):
        return False

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.fort_rush.mono.lobby.tooltips.progression_widget_tooltip():
            return FortRushProgressionWidgetTooltipView()
        return super(FortRushProgressionEntryPointPresenter, self).createToolTipContent(event, contentID)

    def _onLoading(self, *args, **kwargs):
        super(FortRushProgressionEntryPointPresenter, self)._onLoading(*args, **kwargs)
        self._updateModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClick, self.__onWidgetClick),
         (
          self.__itemsCache.onSyncCompleted, self.__onSyncCompleted),
         (
          self.__eventsCache.onSyncCompleted, self._updateModel))

    def _updateModel(self, *_):
        if not self.__ctrl.isEnabled() or not self.__ctrl.isWithinActiveTimeframe():
            return
        currentPoints, stageTotal = self.__ctrl.getCurrentStagePoints()
        with self.viewModel.transaction() as vm:
            vm.setIsAvailable(not self.__ctrl.isFrozen())
            vm.setAllCollected(self.__ctrl.isProgressionCompleted())
            vm.setIsNewItem(self.__ctrl.getTotalProgressionPoints() > getLastSeenProgressionPoints())
            vm.setCurrentProgression(currentPoints)
            vm.setTotalProgression(stageTotal)
            vm.setCurrentProgressionStage(self.__ctrl.getCurrentStageIndex())

    def __onSyncCompleted(self, reason, _):
        if reason != CACHE_SYNC_REASON.CLIENT_UPDATE:
            return
        self._updateModel()

    def __onWidgetClick(self):
        showProgressionView()
