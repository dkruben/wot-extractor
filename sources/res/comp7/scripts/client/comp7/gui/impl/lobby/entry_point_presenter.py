# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/entry_point_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/entry_point_presenter.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import COMP7_UI_SECTION, COMP7_UMG_PROGRESSION_POINTS_SEEN
from comp7.gui.impl.gen.view_models.views.lobby.entry_point_model import EntryPointModel
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers, comp7_shared, comp7_qualification_helpers, account_settings
from comp7.gui.impl.lobby.tooltips.progression_tooltip import ProgressionTooltip
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum
from comp7.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7OverlapCtrlMixin
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from gui.prb_control.entities.listener import IGlobalListener
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from comp7.gui.shared.event_dispatcher import showComp7MetaRootTab
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin

class EntryPointPresenter(TooltipPositionerMixin, Comp7OverlapCtrlMixin, ViewComponent[EntryPointModel], IGlobalListener):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self):
        super(EntryPointPresenter, self).__init__(model=EntryPointModel)

    @property
    def viewModel(self):
        return super(EntryPointPresenter, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        self.initOverlapCtrl()
        self.queueUpdate()
        super(EntryPointPresenter, self)._onLoading(*args, **kwargs)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.comp7.mono.lobby.tooltips.progression_tooltip():
            return ProgressionTooltip()
        return super(EntryPointPresenter, self).createToolTipContent(event, contentID)

    def _updateViewModel(self, *_, **__):
        self.queueUpdate()

    def __updateRating(self, *_, **__):
        activityPoints = self.__comp7Controller.activityPoints
        prevActivityPoints = self.viewModel.getRankInactivityCount()
        if activityPoints != prevActivityPoints:
            self.queueUpdate()

    def _rawUpdate(self):
        super(EntryPointPresenter, self)._rawUpdate()
        if self.__comp7Controller.isFrozen() or not self.__comp7Controller.isEnabled():
            return
        with self.viewModel.transaction() as vm:
            vm.setIsEnabled(not self.__comp7Controller.isOffline)
            vm.setSeasonName(getSeasonNameEnum(self.__comp7Controller, SeasonName))
            vm.setIsEntryPointAnimationSeen(account_settings.getUmgEntryPointSeen())
            self.__updateQualificationData(vm)
            self.__updateProgressionData(vm)

    def __updateQualificationData(self, model):
        comp7_qualification_helpers.setQualificationInfo(model.qualificationModel)

    def __updateProgressionData(self, model):
        if not self.__comp7Controller.isAvailable():
            return
        division = comp7_shared.getPlayerDivision()
        rank = comp7_shared.getRankEnumValue(division)
        rating = self.__comp7Controller.rating
        viewData = self.__comp7Controller.getViewData(R.aliases.comp7.shared.WeeklyQuestsWidget())
        viewData['prevRating'] = rating
        model.setRank(rank)
        model.setCurrentScore(rating)
        model.setPrevScore(self.getPrevUmgProgressionPointsSeen())
        comp7_model_helpers.setDivisionInfo(model=model.divisionInfo, division=division)
        comp7_model_helpers.setElitePercentage(model)
        model.setHasRankInactivity(comp7_shared.hasRankInactivity(rank))
        model.setRankInactivityCount(self.__comp7Controller.activityPoints)

    def _getEvents(self):
        return super(EntryPointPresenter, self)._getEvents() + (
         (
          self.__comp7Controller.onStatusUpdated, self._updateViewModel),
         (
          self.__comp7Controller.onRankUpdated, self.__updateRating),
         (
          self.__comp7Controller.onComp7RanksConfigChanged, self._updateViewModel),
         (
          self.__comp7Controller.onOfflineStatusUpdated, self._updateViewModel),
         (
          self.__comp7Controller.onQualificationBattlesUpdated, self._updateViewModel),
         (
          self.__comp7Controller.onQualificationStateUpdated, self._updateViewModel),
         (
          self.__comp7Controller.onEntitlementsUpdated, self._updateViewModel),
         (
          self.viewModel.onOpenMeta, self.__onOpenMetaClick),
         (
          self.viewModel.onAnimationEnd, self.__onAnimationEnd),
         (
          self.viewModel.onEntryPointAnimationSeen, self.__onEntryPointAnimationSeen))

    @staticmethod
    def __onOpenMetaClick():
        showComp7MetaRootTab()

    def __onAnimationEnd(self):
        self.setUmgProgressionPointsSeen(self.__comp7Controller.rating)

    def __onEntryPointAnimationSeen(self):
        account_settings.markUmgEntryPointSeen()
        self.viewModel.setIsEntryPointAnimationSeen(True)

    @staticmethod
    def setUmgProgressionPointsSeen(curPoints):
        settings = AccountSettings.getUIFlag(COMP7_UI_SECTION)
        settings[COMP7_UMG_PROGRESSION_POINTS_SEEN] = curPoints
        AccountSettings.setUIFlag(COMP7_UI_SECTION, settings)

    @staticmethod
    def getPrevUmgProgressionPointsSeen():
        settings = AccountSettings.getUIFlag(COMP7_UI_SECTION)
        return settings.get(COMP7_UMG_PROGRESSION_POINTS_SEEN, 0)
