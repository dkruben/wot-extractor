# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/header_state_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.page.header.header_state_model import HeaderStateModel as HeaderStateModel, HeaderType as HeaderType
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.utils.callable_delayer import CallableDelayer as CallableDelayer, delayUntilParentWindowReady as delayUntilParentWindowReady
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import Router as Router
from gui.lobby_state_machine.states import LobbyStateFlags as LobbyStateFlags
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class HeaderStatePresenter(IRoutableView):
    __lsm: Any
    __router: Any
    __callableDelayer: Any
    def __init__(self):
        ...
    def getRouterModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onStateChanged(self, routeInfo):
        ...
    def __processRouteChange(self, routeInfo):
        ...
