# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/BrowserController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import Event as Event
from WebBrowser import WebBrowser as WebBrowser
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.game_control.browser_filters import getFilters as _getGlobalFilters
from gui.game_control.gc_constants import BROWSER as BROWSER
from gui.game_control.links import URLMacros as URLMacros
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import BrowserEvent as BrowserEvent, LoadViewEvent as LoadViewEvent
from gui.shared.utils.functions import getViewName as getViewName
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IBrowserController as IBrowserController
from soft_exception import SoftException as SoftException
_logger: Any

class BrowserController(IBrowserController):
    __browsers: Any
    __browsersCallbacks: Any
    __browserCreationCallbacks: Any
    __browserIDGenerator: Any
    __eventMgr: Any
    onBrowserAdded: Any
    onBrowserDeleted: Any
    __urlMacros: Any
    __pendingBrowsers: Any
    __creatingBrowserID: Any
    __filters: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event):
        ...
    def addFilterHandler(self, handler):
        ...
    def removeFilterHandler(self, handler):
        ...
    def nextBrowserID(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def load(self, url=None, title=None, showActionBtn=True, showWaiting=True, browserID=None, isAsync=False, browserSize=None, isDefault=True, callback=None, showCloseBtn=False, useBrowserWindow=True, isModal=False, showCreateWaiting=False, handlers=None, showBrowserCallback=None, isSolidBorder=False):
        ...
    def getAllBrowsers(self):
        ...
    def getBrowser(self, browserID):
        ...
    def delBrowser(self, browserID):
        ...
    def __isCreatingBrowser(self):
        ...
    def __createDone(self, ctx):
        ...
    def __tryCreateNextPendingBrowser(self):
        ...
    def __createBrowser(self, ctx):
        ...
    def __stop(self):
        ...
    def __clearCallbacks(self, browserID, browser, incDelayedCreation):
        ...
    def __showBrowser(self, browserID, ctx):
        ...
