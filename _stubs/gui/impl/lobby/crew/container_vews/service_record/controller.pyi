# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/service_record/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from Event import Event as Event
from gui.impl.lobby.crew.container_vews.common.base_personal_case_controller import BasePersonalCaseController as BasePersonalCaseController
from gui.impl.lobby.crew.container_vews.common.base_personal_case_events import BasePersonalCaseComponentViewEvents as BasePersonalCaseComponentViewEvents
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from typing import Callable as Callable, List as List, Tuple as Tuple
from gui.impl.lobby.container_views.base.events import ComponentEventsBase as ComponentEventsBase

class ServiceRecordInteractionController(BasePersonalCaseController):
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
    def _onCacheResync(self, reason, _):
        ...
    def onChangeTankman(self, tankmanID):
        ...
