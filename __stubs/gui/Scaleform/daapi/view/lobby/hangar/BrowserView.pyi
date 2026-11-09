# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/BrowserView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BrowserScreenMeta import BrowserScreenMeta as BrowserScreenMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.common.sound_constants import BROWSER_VIEW_SOUND_SPACES as BROWSER_VIEW_SOUND_SPACES
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IBrowserController as IBrowserController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class BrowserView(LobbySubView, BrowserScreenMeta):
    __background_alpha__ = 1.0
    _BROWSER_SOUND_SPACE = None
    browserCtrl: Any
    lobbyContext: Any
    __ctx: Any
    __browserId: Any
    __hasFocus: Any
    __browser: Any
    __browserComponent: Any
    __browserParams: Any
    __errorOccurred: Any
    __closedByUser: Any
    __isBrowserLoading: Any
    __pendingRequest: Any
    __viewSize: Any
    def __init__(self, ctx=None):
        ...
    def onFocusChange(self, hasFocus):
        ...
    def onCloseBtnClick(self):
        ...
    def onCloseView(self):
        ...
    def onEscapePress(self):
        ...
    def viewSize(self, width, height):
        ...
    def updateCtx(self, ctx):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _invalidate(self, *args, **kwargs):
        ...
    def _dispose(self):
        ...
    @classmethod
    def __initSoundSpace(cls, soundSpaceID):
        ...
    def __onError(self):
        ...
    def __getFromCtx(self, name, default=None):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self):
        ...
    def __showBrowser(self):
        ...
    def __updateSkipEscape(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __configureBrowser(self):
        ...
    def __navigateTo(self, url):
        ...

def makeBrowserParams(waitingMessage=..., isModal=False, isHidden=False, bgAlpha=1.0, isCloseBtnVisible=False):
    ...
