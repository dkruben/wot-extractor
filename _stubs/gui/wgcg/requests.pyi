# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/requests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG
from gui.clans import formatters as clan_fmts
from gui.clans.settings import DEFAULT_COOLDOWN as DEFAULT_COOLDOWN, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from gui.shared.rq_cooldown import RequestCooldownManager as RequestCooldownManager, REQUEST_SCOPE as REQUEST_SCOPE
from gui.shared.utils.requesters.RequestsController import RequestsController as RequestsController
from gui.shared.utils.requesters.abstract import Response as Response, ClientRequestsByIDProcessor as ClientRequestsByIDProcessor
from gui.wgcg.agate.handlers import AgateRequestHandlers as AgateRequestHandlers
from gui.wgcg.base.handlers import BaseRequestHandlers as BaseRequestHandlers
from gui.wgcg.clan.handlers import ClanRequestHandlers as ClanRequestHandlers
from gui.wgcg.clan_supply.handlers import ClanSupplyRequestHandlers as ClanSupplyRequestHandlers
from gui.wgcg.craftmachine.handlers import CraftmachineRequestHandlers as CraftmachineRequestHandlers
from gui.wgcg.elen.handlers import ElenRequestHandlers as ElenRequestHandlers
from gui.wgcg.external_battle_handlers import BaseExternalBattleUnitRequestHandlers as BaseExternalBattleUnitRequestHandlers
from gui.wgcg.gift_system.handlers import GiftSystemRequestHandlers as GiftSystemRequestHandlers
from gui.wgcg.hof.handlers import HofRequestHandlers as HofRequestHandlers
from gui.wgcg.ingame_tournaments.handlers import IngameTournamentHandlers as IngameTournamentHandlers
from gui.wgcg.loadouts_assistant.handlers import LoadoutsAssistantRequestHandlers as LoadoutsAssistantRequestHandlers
from gui.wgcg.mapbox.handlers import MapboxRequestHandlers as MapboxRequestHandlers
from gui.wgcg.promo_screens.handlers import PromoScreensRequestHandlers as PromoScreensRequestHandlers
from gui.wgcg.rank.handlers import RankRequestHandlers as RankRequestHandlers
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from gui.wgcg.friends_service.handlers import FriendServiceRequestHandlers as FriendServiceRequestHandlers
from gui.wgcg.uilogging.handlers import UILoggingRequestHandlers as UILoggingRequestHandlers
from gui.wgcg.utils.handlers import UtilsRequestHandlers as UtilsRequestHandlers
from gui.wgcg.wot_shop.handlers import WotShopRequestHandlers as WotShopRequestHandlers
from gui.wgcg.w2gt.handlers import W2gtRequestHandlers as W2gtRequestHandlers

class WgcgRequestResponse(Response):
    def isSuccess(self):
        ...
    def getCode(self):
        ...
    def clone(self, data=None):
        ...
    def mergeData(self, data):
        ...
    def getHeaderByKey(self, key, default=None):
        ...
    def getDataByKey(self, key, default=None):
        ...

class WgcgRequester(ClientRequestsByIDProcessor):
    def __init__(self, sender):
        ...
    def doRequestEx(self, ctx, callback, methodName, *args, **kwargs):
        ...
    def _getSenderMethod(self, sender, methodName):
        ...
    def _doCall(self, method, *args, **kwargs):
        ...

class WgcgCooldownManager(RequestCooldownManager):
    def __init__(self):
        ...
    def lookupName(self, rqTypeID):
        ...
    def getDefaultCoolDown(self):
        ...
    def adjust(self, rqTypeID, coolDown=None):
        ...

class WgcgRequestsController(RequestsController):
    __webCtrl: Any
    __handlers: Any
    def __init__(self, webCtrl, requester, cooldown=...):
        ...
    def fini(self):
        ...
    def _getHandlerByRequestType(self, requestTypeID):
        ...
    def _getRequestTimeOut(self):
        ...
