# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/actions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG
from gui.game_control.links import URLMacros as URLMacros
from gui.promo.promo_logger import PromoLogSourceType as PromoLogSourceType
from gui.shared.event_dispatcher import showStrongholds as showStrongholds
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.wgnc.custom_actions_keeper import CustomActionsKeeper as CustomActionsKeeper
from gui.wgnc.events import g_wgncEvents as g_wgncEvents
from gui.wgnc.settings import WGNC_GUI_TYPE as WGNC_GUI_TYPE
from gui.wgnc.common import WebHandlersContainer as WebHandlersContainer
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController, IPromoController as IPromoController, IRankedBattlesController as IRankedBattlesController
from web.web_client_api.sound import HangarSoundWebApi as HangarSoundWebApi
from web.web_client_api import webApiCollection as webApiCollection

# decorador original: @ReprInjector.simple(...)
class _Action(object):
    __slots__: tuple
    _name: Any
    def __init__(self, name):
        ...
    def getName(self):
        ...
    def validate(self, itemsHolder):
        ...
    def invoke(self, notID, actor=None):
        ...

# decorador original: @ReprInjector.withParent(...)
class Callback(_Action):
    __slots__: tuple
    _purge: Any
    _isInvoked: Any
    def __init__(self, name, purge=True):
        ...
    def doPurge(self):
        ...
    def invoke(self, notID, actor=None):
        ...

# decorador original: @ReprInjector.withParent(...)
class _OpenBrowser(_Action):
    __slots__: tuple
    _url: Any
    def __init__(self, name, url):
        ...
    def getURL(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class OpenInternalBrowser(_OpenBrowser, WebHandlersContainer):
    __slots__: tuple
    browserCtrl: Any
    _browserID: Any
    _size: Any
    _showRefresh: Any
    _webHandlerName: Any
    _isSolidBorder: Any
    def __init__(self, name, url, size=None, showRefresh=True, webHandlerName=None, isSolidBorder=False):
        ...
    def invoke(self, _, actor=None):
        ...
    def _getHandlers(self):
        ...
    # decorador original: @adisp_process
    def _doInvoke(self, title):
        ...

# decorador original: @ReprInjector.withParent(...)
class OpenPromoBrowser(OpenInternalBrowser):
    __slots__: tuple
    promoCtrl: Any
    def _doInvoke(self, _):
        ...

# decorador original: @ReprInjector.withParent(...)
class OpenStrongholdBrowser(OpenInternalBrowser):
    __slots__: tuple
    def _doInvoke(self, _):
        ...

# decorador original: @ReprInjector.withParent(...)
class OpenRankedBrowser(OpenInternalBrowser):
    __slots__: tuple
    __rankedController: Any
    def _doInvoke(self, _):
        ...

# decorador original: @ReprInjector.withParent(...)
class OpenExternalBrowser(_OpenBrowser):
    # decorador original: @adisp_process
    def invoke(self, notID, actor=None):
        ...

# decorador original: @ReprInjector.withParent(...)
class CustomAction(_Action):
    actionID: Any
    kwargs: Any
    def __init__(self, action_name, **kwargs):
        ...
    def invoke(self, notID, actor=None):
        ...
    def __getActor(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class OpenWindow(_Action):
    __slots__: tuple
    _target: Any
    def __init__(self, name, target):
        ...
    def validate(self, itemsHolder):
        ...
    def getTarget(self):
        ...
    def invoke(self, notID, actor=None):
        ...

# decorador original: @ReprInjector.withParent(...)
class ReplaceButtons(_Action):
    __slots__: tuple
    _text: Any
    def __init__(self, name, text):
        ...
    def getTextToReplace(self):
        ...
    def invoke(self, notID, actor=None):
        ...

# decorador original: @ReprInjector.simple(...)
class ActionsHolder(object):
    __slots__: tuple
    __actions: Any
    def __init__(self, items):
        ...
    def clear(self):
        ...
    def hasAction(self, name):
        ...
    def hasAllActions(self, names):
        ...
    def getAction(self, name):
        ...
    def validate(self, itemsHolder):
        ...
    def invoke(self, notID, names, actor=None):
        ...

def _getActions4String(value):
    ...
