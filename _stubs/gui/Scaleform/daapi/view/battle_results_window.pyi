# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle_results_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
import constants as constants
from adisp import adisp_process as adisp_process
from constants import PremiumConfigs as PremiumConfigs
from gui import SystemMessages as SystemMessages
from gui import makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.customization.progression_helpers import parseEventID as parseEventID
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS as SOUNDS
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl, getWotPlusShopUrl as getWotPlusShopUrl
from gui.Scaleform.daapi.view.meta.BattleResultsMeta import BattleResultsMeta as BattleResultsMeta
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results import RequestEmblemContext as RequestEmblemContext, EMBLEM_TYPE as EMBLEM_TYPE
from gui.battle_results.settings import PROGRESS_ACTION as PROGRESS_ACTION
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prestige.prestige_helpers import showPrestigeVehicleStats as showPrestigeVehicleStats
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.server_events import events_dispatcher as quests_events
from gui.server_events.events_helpers import isC11nQuest as isC11nQuest
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.event_dispatcher import showProgressiveRewardWindow as showProgressiveRewardWindow, showShop as showShop, showDailyExpPageView as showDailyExpPageView
from gui.sounds.ambients import BattleResultsEnv as BattleResultsEnv
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
_logger: Any

class IBattleResultsComponent(object):
    def setArenaUniqueID(self, arenaUniqueID):
        ...

class BattleResultsWindow(BattleResultsMeta, IGlobalListener):
    __battleResults: Any
    __lobbyContext: Any
    __gameSession: Any
    __appLoader: Any
    __itemsCache: Any
    __sound_env__ = BattleResultsEnv
    __arenaUniqueID: Any
    __dataSet: Any
    def __init__(self, ctx):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def onWindowClose(self):
        ...
    # decorador original: @adisp_process
    def showEventsWindow(self, questID, eventType):
        ...
    def saveSorting(self, iconType, sortDirection, bonusType):
        ...
    def getClanEmblem(self, textureID, clanDBID):
        ...
    def startCSAnimationSound(self, soundEffectID='cs_animation_league_up'):
        ...
    def onResultsSharingBtnPress(self):
        ...
    def showUnlockWindow(self, itemId, unlockType):
        ...
    def showDogTagWindow(self, componentId):
        ...
    def showVehicleStats(self, vehCD):
        ...
    def showProgressiveRewardView(self):
        ...
    def onAppliedPremiumBonus(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onShowDetailsPremium(self):
        ...
    def onShowDetailsWotPlus(self):
        ...
    def onShowManageableXPScreen(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onEnqueued(self, queueType, *args):
        ...
    def onDequeued(self, queueType, *args):
        ...
    # decorador original: @adisp_process
    def __requestClanEmblem(self, textureID, clanDBID):
        ...
    def __setBattleResults(self):
        ...
    def __handleBattleResultsPosted(self, event):
        ...
    def __handleBattleResultsClose(self, _):
        ...
    @classmethod
    def __canNavigate(cls):
        ...
    def __onPremiumStateChanged(self, *_):
        ...
    def __onPremiumXpBonusChanged(self, event):
        ...
    def __onBattleResultWindowShowQuest(self, event):
        ...
    def __updateVO(self, _=None):
        ...
    def __onServerSettingsChange(self, diff):
        ...

def _wrapEmblemUrl(emblemUrl):
    ...
