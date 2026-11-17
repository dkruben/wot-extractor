# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/cache_providers/stronghold_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.clans.cache_providers.base_provider import IBaseProvider as IBaseProvider
from gui.clans.clan_helpers import isStrongholdsEnabled as isStrongholdsEnabled
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.wgnc.actions import OpenInternalBrowser as OpenInternalBrowser
from gui.wgnc.proxy_data import ShowInBrowserItem as ShowInBrowserItem
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class ClientStrongholdProvider(IBaseProvider, IGlobalListener):
    lobbyContext: Any
    browserCtrl: Any
    __tabActive: Any
    __entityActive: Any
    __unitActive: Any
    __browserID: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self, withClear=False):
        ...
    def onPrbEntitySwitched(self):
        ...
    def isTabActive(self):
        ...
    def loadUrl(self, url):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    # decorador original: @adisp_process
    def __leave(self):
        ...
    def __checkSwitch(self):
        ...
    def __onStrongholdsActivate(self, _):
        ...
    def __onStrongholdsDeactivate(self, _):
        ...
    def __onStrogholdLoaded(self, event):
        ...
    # decorador original: @adisp_process
    def __showPopupDlg(self):
        ...
