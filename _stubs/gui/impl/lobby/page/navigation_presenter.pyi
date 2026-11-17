# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/navigation_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.page.header.navigation_bar_info_button import NavigationBarInfoButton as NavigationBarInfoButton, ButtonType as ButtonType
from gui.impl.gen.view_models.views.lobby.page.header.navigation_bar_model import NavigationBarModel as NavigationBarModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.utils.callable_delayer import CallableDelayer as CallableDelayer, delayUntilParentWindowReady as delayUntilParentWindowReady
from gui.lobby_state_machine.states import LobbyStateFlags as LobbyStateFlags, LobbyStateDescription as LobbyStateDescription
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers.events_handler import EventsHandler as EventsHandler
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
_logger: Any
_NAVIGATION_ACTION_TARGET_KEY = 'name'
_INFO_ACTION_INDEX_KEY = 'index'

# base nao representavel no stub: ViewComponent[...]
class NavigationPresenter(EventsHandler):
    __DESC_TO_BUTTON_TYPE: dict
    __callableDelayer: Any
    __lsm: Any
    __visibleState: Any
    __infoActionHandlers: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __routeChanged(self, routeInfo):
        ...
    def __processRouteChange(self, routeInfo):
        ...
    def __onNavigate(self, navigationAction):
        ...
    def __onInfoAction(self, infoAction):
        ...
