# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/common/base_personal_case_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from Event import Event as Event
from gui.impl.dialogs.dialogs import showRetrainSingleDialog as showRetrainSingleDialog
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.crew.container_vews.common.base_personal_case_events import BasePersonalCaseComponentViewEvents as BasePersonalCaseComponentViewEvents
from gui.shared import event_dispatcher as event_dispatcher
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import Callable as Callable, List as List, Tuple as Tuple
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.container_views.base.events import ComponentEventsBase as ComponentEventsBase

class BasePersonalCaseController(InteractionController):
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
    def _onChangeVehicleClick(self, tankmanInvID):
        ...
    # decorador original: @wg_async
    def _onRetrainClick(self):
        ...
