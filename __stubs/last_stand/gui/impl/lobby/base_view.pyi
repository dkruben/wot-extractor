# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/base_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow, LobbyNotificationWindow as LobbyNotificationWindow
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from last_stand.skeletons.ls_controller import ILSController as ILSController
from skeletons.gui.app_loader import IAppLoader as IAppLoader

class BaseView(ViewImpl, IGlobalListener):
    lsCtrl: Any
    def onPrbEntitySwitched(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onEventDisabled(self):
        ...
    def _onClose(self):
        ...

class SwitcherPresenter(ViewComponent, IGlobalListener):
    lsCtrl: Any
    def __init__(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onEventDisabled(self):
        ...
    def _onClose(self):
        ...

class EventLobbyWindow(LobbyWindow):
    __appLoader: Any
    _blur: Any
    def __init__(self, wndFlags, decorator=None, content=None, parent=None, layer=...):
        ...
    def _initialize(self):
        ...
    def __onViewLoaded(self, _, *args):
        ...
    def _finalize(self):
        ...

class EventLobbyNotificationWindow(LobbyNotificationWindow):
    __appLoader: Any
    _blur: Any
    def __init__(self, wndFlags, decorator=None, content=None, parent=None, layer=...):
        ...
    def load(self):
        ...
    def _initialize(self):
        ...
    def __onViewLoaded(self, _, *args):
        ...
    def _finalize(self):
        ...
