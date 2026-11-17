# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/PromoController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from Event import Event as Event, EventManager as EventManager
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams as GuiImplViewLoadParams
from gui.app_loader import sf_lobby as sf_lobby
from gui.game_control import gc_constants as gc_constants
from gui.game_control.links import URLMacros as URLMacros
from gui.impl.lobby.common.browser_view import BrowserView as BrowserView, makeSettings as makeSettings
from gui.impl.gen import R as R
from gui.promo.promo_logger import PromoLogSourceType as PromoLogSourceType, PromoLogActions as PromoLogActions, PromoLogSubjectType as PromoLogSubjectType
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.events import BrowserEvent as BrowserEvent
from gui.shared.utils import isPopupsWindowsOpenDisabled as isPopupsWindowsOpenDisabled
from gui.wgcg.promo_screens.contexts import PromoGetTeaserRequestCtx as PromoGetTeaserRequestCtx, PromoSendTeaserShownRequestCtx as PromoSendTeaserShownRequestCtx, PromoGetUnreadCountRequestCtx as PromoGetUnreadCountRequestCtx
from helpers import isPlayerAccount as isPlayerAccount, dependency as dependency
from helpers.http import url_formatters as url_formatters
from shared_utils import findFirst as findFirst
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IPromoController as IPromoController, IBrowserController as IBrowserController, IEventsNotificationsController as IEventsNotificationsController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gui.shared.promo import IPromoLogger as IPromoLogger
from skeletons.gui.web import IWebController as IWebController
from web.web_client_api import webApiCollection as webApiCollection, ui as ui_web_api, sound as sound_web_api
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.platform import PlatformWebApi as PlatformWebApi
from web.web_client_api.promo import PromoWebApi as PromoWebApi
from web.web_client_api.battle_pass import BattlePassWebApi as BattlePassWebApi
from web.web_client_api.ranked_battles import RankedBattlesWebApi as RankedBattlesWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.social import SocialWebApi as SocialWebApi
from web.web_client_api.vehicles import VehiclesWebApi as VehiclesWebApi
from web.web_client_api.blueprints_convert_sale import BlueprintsConvertSaleWebApi as BlueprintsConvertSaleWebApi
from frameworks.wulf import View as View
_PromoData: Any
_logger: Any

class PromoController(IPromoController):
    __browserCtrl: Any
    __notificationsCtrl: Any
    __webController: Any
    __settingsCore: Any
    __lobbyContext: Any
    __logger: Any
    __loginManager: Any
    __urlMacros: Any
    __externalCloseCallback: Any
    __isLobbyInited: Any
    __pendingPromo: Any
    __promoCount: Any
    __lastUpdateTimeMark: Any
    __promoData: Any
    __waitingForWebBridgeData: Any
    __battlesFromLastTeaser: Any
    __wasInBattle: Any
    __hasPendingTeaser: Any
    __isPromoOpen: Any
    __browserCreationCallbacks: Any
    __browserWatchers: Any
    __isTeaserOpen: Any
    __checkIntervalInBattles: Any
    __em: Any
    onNewTeaserReceived: Any
    onPromoCountChanged: Any
    onTeaserShown: Any
    onTeaserClosed: Any
    def __init__(self):
        ...
    @property
    def isPromoOpen(self):
        ...
    # decorador original: @sf_lobby
    def app(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    @property
    def checkIntervalInBattles(self):
        ...
    def setNewTeaserData(self, teaserData):
        ...
    def showFieldPost(self):
        ...
    # decorador original: @adisp_process
    def showLastTeaserPromo(self):
        ...
    def setUnreadPromoCount(self, count):
        ...
    def isTeaserOpen(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def isActive(self):
        ...
    def getPromoCount(self):
        ...
    def showPromo(self, url, closeCallback=None, source=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getUrlWithAuthParams(self, url, callback):
        ...
    def subscribePresenter(self, presentCb):
        ...
    def unsubscribePresenter(self, presentCb):
        ...
    def __needToGetTeasersInfo(self):
        ...
    def __onTeaserClosed(self, byUser=False):
        ...
    # decorador original: @adisp_process
    def __updateWebBrgData(self):
        ...
    def __onPromoClosed(self, **kwargs):
        ...
    # decorador original: @adisp_process
    def __requestPromoCount(self):
        ...
    def __updatePromoCount(self, count):
        ...
    def __updateTeaserData(self, teaserData):
        ...
    def __showTeaser(self):
        ...
    # decorador original: @adisp_process
    def __onTeaserShown(self, promoID):
        ...
    def __tryToShowTeaser(self):
        ...
    def __stop(self):
        ...
    def __processPromo(self, promos):
        ...
    def __onEventNotification(self, added, _):
        ...
    def __registerAndShowPromoBrowser(self, url, closeCallback, loadingCallback):
        ...
    # decorador original: @adisp_process
    def __showBrowserView(self, url, loadingCallback=None, soundSpaceID=None):
        ...
    def __registerLoadingCallback(self, url, callback):
        ...
    def __handleBrowserCreated(self, event):
        ...
    def __clearWatcher(self, browserID):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __addAuthParams(self, url, callback):
        ...
    def __addSteamParams(self, url):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _showBrowserView(url, returnClb, soundSpaceID=None, guiLoader=None):
    ...
