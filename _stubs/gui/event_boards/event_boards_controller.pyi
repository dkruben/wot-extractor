# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/event_boards/event_boards_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import constants as constants
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ELEN_NOTIFICATIONS as ELEN_NOTIFICATIONS
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from gui import SystemMessages as SystemMessages
from gui.Scaleform.genConsts.MISSIONS_CONSTANTS import MISSIONS_CONSTANTS as MISSIONS_CONSTANTS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.event_boards.event_boards_items import EventBoardsSettings as EventBoardsSettings, HangarFlagData as HangarFlagData, LeaderBoard as LeaderBoard, IPlayerProgression as IPlayerProgression, MyInfoInLeaderBoard as MyInfoInLeaderBoard, SET_DATA_STATUS_CODE as SET_DATA_STATUS_CODE, EVENT_STATE as EVENT_STATE, PLAYER_STATE_REASON as _psr
from gui.event_boards.listener import IEventBoardsListener as IEventBoardsListener
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.utils.requesters.abstract import Response as Response
from gui.wgcg import IWebController as IWebController
from gui.wgcg.elen.contexts import EventBoardsGetEventDataCtx as EventBoardsGetEventDataCtx, EventBoardsGetPlayerDataCtx as EventBoardsGetPlayerDataCtx, EventBoardsJoinEventCtx as EventBoardsJoinEventCtx, EventBoardsLeaveEventCtx as EventBoardsLeaveEventCtx, EventBoardsGetMyEventTopCtx as EventBoardsGetMyEventTopCtx, EventBoardsGetMyLeaderboardPositionCtx as EventBoardsGetMyLeaderboardPositionCtx, EventBoardsGetLeaderboardCtx as EventBoardsGetLeaderboardCtx, EventBoardsGetHangarFlagCtx as EventBoardsGetHangarFlagCtx, EventBoardsGetPlayerProgressionCtx as EventBoardsGetPlayerProgressionCtx
from gui.wgcg.settings import WebRequestDataType as _crdt
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Any as Any, Callable as Callable, Type as Type
from gui.event_boards.event_boards_items import EventSettings as EventSettings
_logger: _Any
SUCCESS_STATUSES: tuple

class EventBoardsController(IEventBoardController, IEventBoardsListener, IGlobalListener):
    clanController: _Any
    connectionMgr: _Any
    itemsCache: _Any
    __isLoggedIn: _Any
    __eventBoardsSettings: _Any
    __hangarFlagData: _Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def isElenQuestsStatusWrong(self, currentEvent):
        ...
    def getPlayerEventsData(self):
        ...
    def getEventsSettingsData(self):
        ...
    def hasEvents(self):
        ...
    def getMyEventsTopData(self):
        ...
    def getHangarFlagData(self):
        ...
    def updateHangarFlag(self):
        ...
    def cleanEventsData(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def sendRequest(self, ctx, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def joinEvent(self, eventID, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def leaveEvent(self, eventID, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getHangarFlag(self, callback, onLogin=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getEvents(self, callback, onlySettings=False, isTabVisited=False, onLogin=False, prefetchKeyArtBig=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getMyLeaderboardInfo(self, eventID, leaderboardID, callback, showNotification=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getLeaderboard(self, eventID, leaderboardID, pageNumber, callback, leaderBoardClass=None, showNotification=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getPlayerProgression(self, eventID, leaderboardID, progressionClass, callback=None, showNotification=True):
        ...
    def __checkStartedFinishedEvents(self, isTabVisited):
        ...
    def __handleResponseNotifications(self, response, ctx):
        ...
    def __handleJoinEventNotification(self, response, ctx):
        ...
    def __handleLeaveEventNotification(self, response, ctx):
        ...
    def __getAvailableVehicles(self, vehicleIds):
        ...
    @staticmethod
    def __isSuccessResponse(response):
        ...
    @staticmethod
    def __complexWarningNotification(header, body):
        ...
    @staticmethod
    def __standardErrorNotification():
        ...
