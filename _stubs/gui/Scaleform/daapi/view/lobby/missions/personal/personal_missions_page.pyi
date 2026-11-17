# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import operator as operator
from collections import namedtuple as namedtuple
from future.utils import lfilter as lfilter, viewvalues as viewvalues
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_BUTTONS import PERSONAL_MISSIONS_BUTTONS as PERSONAL_MISSIONS_BUTTONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.missions import missions_helper as missions_helper
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getHtmlAwardSheetIcon as getHtmlAwardSheetIcon, getSuitableVehicles as getSuitableVehicles, isBranchesStarted as isBranchesStarted, switchCampaign as switchCampaign, processOperation as processOperation, isSuitableBranchForPawn as isSuitableBranchForPawn
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import getChainVehRequirements as getChainVehRequirements
from gui.Scaleform.daapi.view.meta.PersonalMissionsPageMeta import PersonalMissionsPageMeta as PersonalMissionsPageMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl.lobby.personal_missions_30.personal_mission_constants import PERSONAL_MISSIONS_CAMPAIGNS_1_2_SPACE as PERSONAL_MISSIONS_CAMPAIGNS_1_2_SPACE
from gui.server_events.event_items import PersonalMission as PersonalMission
from gui.server_events.events_dispatcher import showPersonalMissionDetails as showPersonalMissionDetails, hidePersonalMissionDetails as hidePersonalMissionDetails, showPersonalMissionAwards as showPersonalMissionAwards
from gui.server_events.events_helpers import AwardSheetPresenter as AwardSheetPresenter
from gui.server_events.finders import getBranchByOperationId as getBranchByOperationId
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation as PersonalMissionsNavigation
from gui.server_events.pm_constants import SOUNDS as SOUNDS, PM_TUTOR_FIELDS as _PTF
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.event_dispatcher import showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow
from gui.shared.events import PersonalMissionsEvent as PersonalMissionsEvent, LoadViewEvent as LoadViewEvent
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items.Vehicle import getTypeShortUserName as getTypeShortUserName
from gui.shared.gui_items.processors import quests as quests
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency, int2roman as int2roman
from helpers.i18n import makeString as _ms
from personal_missions import PM_BRANCH as PM_BRANCH, PM_BRANCH_TO_FINAL_PAWN_COST as PM_BRANCH_TO_FINAL_PAWN_COST, PERSONAL_MISSION_REGULAR_MIN_LEVEL as PERSONAL_MISSION_REGULAR_MIN_LEVEL
from shared_utils import findFirst as findFirst, first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.server_events import IEventsCache as IEventsCache
_logger: Any
_ChainState: Any
_BranchState: Any
_UI_CHAINS_LEN: dict

class PersonalMissionsPage(LobbySubView, PersonalMissionsPageMeta, PersonalMissionsNavigation):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_CAMPAIGNS_1_2_SPACE
    __settingsCore: Any
    __eventsCache: Any
    __mapView: Any
    __eventID: Any
    __lastTutorState: Any
    __backAlias: Any
    __callbackID: Any
    __isPersonalMissionDetailsVisible: Any
    def __init__(self, ctx):
        ...
    def showAwards(self):
        ...
    def onBarClick(self, chainID, operationIdx):
        ...
    def onSkipTaskClick(self, btnID):
        ...
    def switchToAnotherOperation(self, operationId, chainId):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _selectInitialMissions(self, campaignToActive, operationToActive):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _switchCampaign(self, campaignToActive):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _activateCampaign(self, campaignToActive, operationToActive):
        ...
    def closeView(self):
        ...
    def onTutorialAcceptBtnClicked(self):
        ...
    def onBackBtnClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _invalidate(self, ctx=None):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __collectSideBarData(self):
        ...
    @property
    def __PMCache(self):
        ...
    def __onDetailsViewOpen(self, _):
        ...
    def __onDetailsViewClose(self, _):
        ...
    def __initialize(self, ctx=None):
        ...
    def __updateComponents(self):
        ...
    def __updateMapData(self):
        ...
    def __getProgress(self, pmQuests):
        ...
    def __updateHeader(self):
        ...
    def __updateFooter(self):
        ...
    def __getSheetsBlockData(self):
        ...
    def __getNoVehicleStatusLabel(self, useIcon):
        ...
    def __updateSideBar(self):
        ...
    def __getOperationTitle(self):
        ...
    def __getChainState(self, pmQuests):
        ...
    def __getBranchState(self, branch):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __pawnMission(self, questInProgress):
        ...
    def __onQuestsUpdated(self, *args):
        ...
    def __tryOpenMissionDetails(self):
        ...
    def __getLastQuest(self):
        ...
    def __getTutorMultipleState(self):
        ...
    def __getTutorSingleState(self):
        ...
    def __checkTutorState(self):
        ...
    def __navigateTo(self, operationID=None, chainID=None):
        ...
    def __resetToIncomplete(self):
        ...
    def __showTutor(self, tutorState, showPawned=False):
        ...
    def _packFirstShowAwardTutorData(self):
        ...
    def __packUseFreeSheetsAwardTutorData(self, hasPawned):
        ...
