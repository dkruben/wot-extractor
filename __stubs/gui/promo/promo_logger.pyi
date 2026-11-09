# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/promo/promo_logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from future.utils import listitems as listitems
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from gui.macroses import getLanguageCode as getLanguageCode
from gui.wgcg.promo_screens.contexts import PromoSendActionLogCtx as PromoSendActionLogCtx
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount, time_utils as time_utils
from ids_generators import Int32IDGenerator as Int32IDGenerator
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared.promo import IPromoLogger as IPromoLogger
from skeletons.gui.web import IWebController as IWebController
_logger: Any

class PromoLogActions(CONST_CONTAINER):
    RECEIVED_WGNC = 'ReceivedWGNC'
    GET_MOST_IMPORTANT = 'GetMostImportant'
    OPEN_FROM_TEASER = 'OpenFromTeaser'
    CLOSED_BY_USER = 'ClosedByUser'
    KILLED_BY_SYSTEM = 'KilledBySystem'
    OPEN_FROM_MENU = 'OpenFromMenu'
    OPEN_IN_OLD = 'OpenInOld'

class PromoLogSubjectType(CONST_CONTAINER):
    TEASER = 'Teaser'
    PROMO_SCREEN = 'Promoscreen'
    INDEX = 'Index'
    PROMO_SCREEN_OR_INDEX = 'PromoscreenOrIndex'

class PromoLogSourceType(CONST_CONTAINER):
    WGNC = 'WGNC'
    FIRST_LOGIN = 'Firstlogin'
    AFTER_BATTLE = '10stBattle'
    PRMP = 'PRMP'
    SSE = 'SSE'

class PromoLogger(IPromoLogger):
    __PARAMS_MAP: dict
    __TEASER_PARAMS_MAP: dict
    __lobbyContext: Any
    __webController: Any
    __ANSWER_WAITING_TIME = 30
    __IDGenerator: Any
    __requestIDs: Any
    def __init__(self):
        ...
    # decorador original: @adisp_process
    def logAction(self, **kwargs):
        ...
    def logTeaserAction(self, teaserData, **kwargs):
        ...
    def getLoggingFuture(self, teaserData=None, **kwargs):
        ...
    def fini(self):
        ...
    def __isEnabled(self):
        ...
    def __sendDelayed(self, teaserData, requestID, callbackID=None, **kwargs):
        ...
    def __packData(self, data):
        ...

def _getPlayerDatabaseID():
    ...
