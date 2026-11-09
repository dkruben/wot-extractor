# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/info_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from frameworks.wulf import Window as Window
from gui.impl.gen.view_models.views.lobby.common.info_view_model import InfoViewModel as InfoViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_logger: Any
DEFAULT_CONTENT_DATA: Any

class InfoView(ViewImpl):
    def __init__(self, settings, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...

# base nao representavel no stub: typing.NamedTuple(...)
class ContentData:
    def createContent(self, layoutID):
        ...

class IInfoWindowProcessor(object):
    def showAllowed(self):
        ...
    def setShown(self):
        ...
    def show(self, parent=None):
        ...

class _InfoWindow(LobbyWindow):
    __slots__: tuple
    __closeCallback: Any
    def __init__(self, layoutID, parent, contentData, wndFlags, callback):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def __onDisconnected(self):
        ...

class _InfoWindowProcessor(IInfoWindowProcessor):
    __slots__: tuple
    __settingsCore: Any
    layoutID: Any
    contentData: Any
    uiStorageKey: Any
    wndFlags: Any
    def __init__(self, layoutID, contentData, uiStorageKey, wndFlags):
        ...
    def showAllowed(self):
        ...
    def setShown(self):
        ...
    # decorador original: @wg_async.wg_async
    def show(self, parent=None):
        ...
    def __loadWindow(self, parent, callback):
        ...

def createContentData(clazz, modelClazz=..., *args, **kwargs):
    ...
def getInfoWindowProc(layoutID, contentData=..., uiStorageKey=None, wndFlags=...):
    ...
