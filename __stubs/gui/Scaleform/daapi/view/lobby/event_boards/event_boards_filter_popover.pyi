# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_filter_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeFiltersVO as makeFiltersVO
from gui.Scaleform.daapi.view.meta.EventBoardsResultFilterPopoverViewMeta import EventBoardsResultFilterPopoverViewMeta as EventBoardsResultFilterPopoverViewMeta
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.shared.utils.functions import makeTooltip as makeTooltip

class EventBoardsFilterPopover(EventBoardsResultFilterPopoverViewMeta):
    caller: Any
    eventID: Any
    __onChangeFilter: Any
    def __init__(self, ctx=None):
        ...
    def changeFilter(self, lid):
        ...
    def onWindowClose(self):
        ...
    def setData(self, eventData, onApply, leaderboardID=None):
        ...
