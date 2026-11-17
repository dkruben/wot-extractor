# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import Event as Event
from Account import PlayerAccount as PlayerAccount
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, PREMIUM_TYPE as PREMIUM_TYPE, PlayerSatisfactionRating as PlayerSatisfactionRating
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from frameworks.wulf import WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.battle_results import context as context, emblems as emblems, reusable as reusable, stored_sorting as stored_sorting
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage as pushNoBattleResultsDataMessage
from gui.battle_results.composer import RegularStatsComposer as RegularStatsComposer
from gui.battle_results.random_stats_ctrl import RandomBattleResultStatsCtrl as RandomBattleResultStatsCtrl
from gui.battle_results.settings import PREMIUM_STATE as PREMIUM_STATE
from gui.shared import event_dispatcher as event_dispatcher, events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.processors.common import BattleResultsGetter as BattleResultsGetter, PremiumBonusApplier as PremiumBonusApplier
from gui.shared.gui_items.processors.player_satisfaction_rating import PlayerSatisfactionRatingProcessor as PlayerSatisfactionRatingProcessor
from gui.shared.system_factory import collectBattleResultStatsCtrl as collectBattleResultStatsCtrl
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from helpers.func_utils import isDeveloperFunc as isDeveloperFunc
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl as IBattleResultStatsCtrl
from items import vehicles as vehicles
_logger: Any
g_pbsFakeData: Any

class _PostBattleFakeData(object):
    __itemsCache: Any
    defaultPBS: Any
    vehicleAndOffsets: Any
    vehCameraSmallOffset: Any
    vehCameraMediumOffset: Any
    vehicleName: Any
    def __init__(self):
        ...
    def getVehicle(self):
        ...
    def getStatsCtrl(self, battleResults):
        ...
    def switchPBS(self):
        ...

class PostBattleResultsStateMixin(object):
    ...

class BattleResultsService(IBattleResultsService):
    battleMatters: Any
    itemsCache: Any
    lobbyContext: Any
    sessionProvider: Any
    wotPlusController: Any
    appLoader: Any
    __slots__: tuple
    __statsCtrls: Any
    __buy: Any
    __appliedAddXPBonus: Any
    __eventsManager: Any
    __playerSatisfactionRatings: Any
    onResultPosted: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def requestResults(self, ctx, callback=None):
        ...
    # decorador original: @adisp_async
    def requestEmblem(self, ctx, callback=None):
        ...
    def postResult(self, result, needToShowUI=True):
        ...
    def areResultsPosted(self, arenaUniqueID):
        ...
    def getResultsVO(self, arenaUniqueID):
        ...
    def getStatsCtrl(self, arenaUniqueID):
        ...
    def saveStatsSorting(self, bonusType, iconType, sortDirection):
        ...
    # decorador original: @decorators.adisp_process(...)
    def applyAdditionalBonus(self, arenaUniqueID):
        ...
    def isAddXPBonusApplied(self, arenaUniqueID):
        ...
    def isAddXPBonusEnabled(self, arenaUniqueID):
        ...
    def getAdditionalXPValue(self, arenaUniqueID):
        ...
    # decorador original: @adisp_process
    def submitPlayerSatisfactionRating(self, arenaUniqueID, rating):
        ...
    def getPlayerSatisfactionRating(self, arenaUniqueID):
        ...
    # decorador original: @isDeveloperFunc
    def resetPlayerSatisfactionRatings(self):
        ...
    def isCrewSameForArena(self, arenaUniqueID):
        ...
    def isXPToTManSameForArena(self, arenaUniqueID):
        ...
    def getVehicleForArena(self, arenaUniqueID):
        ...
    def notifyBattleResultsPosted(self, arenaUniqueID, needToShowUI=False):
        ...
    def __postStatistics(self, reusableInfo, result):
        ...
    def __getAdditionalXPBattles(self):
        ...
    # decorador original: @adisp_process
    def __showResults(self, ctx):
        ...
    def __isSwitchEnabled(self, statsCtrl):
        ...
    def __notifyBattleResultsPosted(self, arenaUniqueID, needToShowUI=False):
        ...
    def __handleLobbyViewLoaded(self, _):
        ...
    def __onViewLoaded(self, view):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __updateStatsCtrl(self, arenaUniqueID, xpBonusData, callback):
        ...
    def __updateReusableInfo(self, reusableInfo, xpBonusData=None):
        ...
    def __onPremiumBought(self, event):
        ...
    def __makePremiumState(self, arenaUniqueID, premType=...):
        ...
    def __onAddXPBonusChanged(self, isBonusApplied=True):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def waitForBattleResults(self, arenaUniqueID, callback=None):
        ...

class _PostBattleStatesObserver(BaseStateObserver):
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...

def createStatsCtrl(reusableInfo):
    ...
