# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_details_container_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.EventBoardsDetailsContainerViewMeta import EventBoardsDetailsContainerViewMeta as EventBoardsDetailsContainerViewMeta
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController

class EventBoardsDetailsContainerView(EventBoardsDetailsContainerViewMeta):
    eventsController: Any
    _linkage = None
    _extra: dict
    ctx: Any
    eventData: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __handleDetailsClose(self, _):
        ...

class EventBoardsDetailsBrowserView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_BROWSER_LINKAGE

class EventBoardsDetailsVehiclesView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_VEHICLES_LINKAGE

class EventBoardsDetailsAwardsView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_AWARDS_LINKAGE
    _extra: dict

class EventBoardsDetailsBattleView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_BATTLE_LINKAGE
    _extra: dict
