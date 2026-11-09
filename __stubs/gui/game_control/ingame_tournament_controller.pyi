# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/ingame_tournament_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems, viewvalues as viewvalues
from adisp import adisp_process as adisp_process
from gui.shared.event_dispatcher import showOfferGiftsWindow as showOfferGiftsWindow
from shared_utils import findFirst as findFirst, first as first
from Event import EventManager as EventManager, Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.AccountSettings import AccountSettings as AccountSettings, INGAME_TOURNAMENT_SECTION as INGAME_TOURNAMENT_SECTION, INGAME_TOURNAMENT_WCI_INTRO_SEEN as INGAME_TOURNAMENT_WCI_INTRO_SEEN, INGAME_TOURNAMENT_OLS_INTRO_SEEN as INGAME_TOURNAMENT_OLS_INTRO_SEEN
from constants import CURRENT_REALM as CURRENT_REALM
from constants import Configs as Configs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getShopURL as getShopURL
from gui.game_control.links import URLMacros as URLMacros
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shop import showIngameShop as showIngameShop
from gui.wgcg import IWebController as IWebController
from gui.wgcg.ingame_tournaments.context import IngameTournamentGetDataCtx as IngameTournamentGetDataCtx
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.ingame_tournament_helper import IngameTournamentState as IngameTournamentState, IngameTournamentMatchState as IngameTournamentMatchState, IngameTournamentUrlType as IngameTournamentUrlType, IngameTournamentLogoSize as IngameTournamentLogoSize, IngameTournamentBracketType as IngameTournamentBracketType, IngameTournamentType as IngameTournamentType
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from skeletons.gui.game_control import IIngameTournamentController as IIngameTournamentController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
_logger: Any

# base nao representavel no stub: typing.NamedTuple(...)
class _TeamData:
    @classmethod
    def fromParamsDict(cls, params):
        ...
    @staticmethod
    def __getLogoSizeByStr(logoSizeStr):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _MatchData:
    @classmethod
    def fromParamsDict(cls, params, bracketType, stageIndex):
        ...
    @property
    def state(self):
        ...
    @property
    def bestOf(self):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _GroupData:
    @classmethod
    def fromParamsDict(cls, params, bracketType, stageIndex):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _StageData:
    @classmethod
    def fromParamsDict(cls, params, stageIndex):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _RewardData:
    @classmethod
    def fromParamsDict(cls, params):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _LeaderboardData:
    @classmethod
    def fromParamsData(cls, paramsData):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _PrizePoolData:
    @classmethod
    def fromParamsData(cls, paramsData):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class _IngameTournamentData:
    @classmethod
    def fromRequestResponse(cls, wgcgResponse):
        ...
    def getLiveMatch(self):
        ...
    def getUpcomingMatches(self):
        ...
    def getAllMatches(self):
        ...
    def getTotalRewardAmount(self):
        ...
    def getLastPrizePoolUpdate(self):
        ...
    def isDynamicPrizePool(self):
        ...
    def getLeaderboardDataByTeam(self, teamID):
        ...
    def getRewardForPosition(self, position):
        ...
    @classmethod
    def __getStreamUrlData(cls, params):
        ...

class IngameTournamentController(IIngameTournamentController, IGlobalListener):
    __lobbyContext: Any
    __webCtrl: Any
    __eventsService: Any
    __offersProvider: Any
    __serverSettings: Any
    __availabilityByTournamentType: Any
    __callbackDelayer: Any
    __eventsManager: Any
    onTournamentEntryPointUpdated: Any
    onTournamentWGCGDataUpdated: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def isTournamentAvailable(self, tournamentType):
        ...
    def getTournamentState(self, tournamentType):
        ...
    def getCurrentShowmatch(self, tournamentType):
        ...
    def getNextShowmatch(self, tournamentType):
        ...
    def getTournamentShowmatchPeriod(self, tournamentType):
        ...
    def getIsIntroSeen(self, tournamentType):
        ...
    def setIsIntroSeen(self, tournamentType):
        ...
    # decorador original: @adisp_process
    def requestTournamentWGCGData(self):
        ...
    def getTokenStoreOpeningTime(self, tournamentType):
        ...
    def getOfferGiftsToken(self, tournamentType):
        ...
    def openOfferGifts(self, tournamentType, overrideOnBackCallback=None):
        ...
    # decorador original: @adisp_process
    def openShop(self, tournamentType):
        ...
    def __onPrbDispatcherCreated(self):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __onConfigUpdated(self, serverSettingsDiff):
        ...
    def __updateTournamentEntryPoint(self):
        ...
    def __getNextUpdateTimestamp(self):
        ...
    def __getConfig(self):
        ...
    def __getConfigByTournamentType(self, tournamentType):
        ...
