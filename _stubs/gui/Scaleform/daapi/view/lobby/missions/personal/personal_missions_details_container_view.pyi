# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_details_container_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from operator import methodcaller as methodcaller
from future.utils import viewvalues as viewvalues
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getDetailedMissionData as getDetailedMissionData, getMapRegionTooltipData as getMapRegionTooltipData, isBranchesStarted as isBranchesStarted, switchCampaign as switchCampaign, isSuitableBranchForPawn as isSuitableBranchForPawn
from gui.Scaleform.daapi.view.meta.PersonalMissionDetailsContainerViewMeta import PersonalMissionDetailsContainerViewMeta as PersonalMissionDetailsContainerViewMeta
from gui.server_events.pm_constants import PM_SUIT_OP_PLUGIN_ERR_RESPONSE as PM_SUIT_OP_PLUGIN_ERR_RESPONSE
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.events import PersonalMissionsEvent as PersonalMissionsEvent
from gui.shared.gui_items.processors import quests as quests_proc
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
_logger: Any

class PersonalMissionDetailsContainerView(LobbySubView, PersonalMissionDetailsContainerViewMeta):
    _lobbyCtx: Any
    _eventsCache: Any
    __selectedQuestID: Any
    __storage: Any
    __quests: Any
    __branch: Any
    __operationID: Any
    __datailedList: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def useSheet(self, eventID):
        ...
    def startMission(self, eventID):
        ...
    def obtainAward(self, eventID):
        ...
    def requestMissionData(self, index):
        ...
    def changePage(self, eventID):
        ...
    def discardMission(self, eventID):
        ...
    def retryMission(self, eventID):
        ...
    def onPauseClick(self, eventID):
        ...
    def _initialize(self, ctx=None):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _selectMission(self, quest):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _processMission(self, eventID):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _discardMission(self, eventID):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _pauseMission(self, eventID):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _pawnMission(self, eventID):
        ...
    def _populate(self):
        ...
    def _invalidate(self, ctx=None):
        ...
    def _dispose(self):
        ...
    def _onProgressUpdated(self, branch):
        ...
    def __handleDetailsClose(self, _):
        ...
    def __getQuests(self):
        ...
    def __setData(self):
        ...
    def __setMayPawnForQuest(self, quest):
        ...
    def _onSettingsChanged(self, diff):
        ...
