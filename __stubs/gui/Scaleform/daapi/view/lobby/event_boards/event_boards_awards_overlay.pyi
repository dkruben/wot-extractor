# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_awards_overlay.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeFiltersVO as makeFiltersVO, vehicleValueGetter as vehicleValueGetter
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleBasicVO as makeVehicleBasicVO
from gui.Scaleform.daapi.view.meta.EventBoardsAwardsOverlayMeta import EventBoardsAwardsOverlayMeta as EventBoardsAwardsOverlayMeta
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.event_boards.event_boards_items import EVENT_TYPE as EVENT_TYPE
from gui.server_events.awards_formatters import QuestsBonusComposer as QuestsBonusComposer, getEventBoardsAwardPacker as getEventBoardsAwardPacker
from gui.shared.utils import sortByFields as sortByFields
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import int2roman as int2roman, dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache

class EventBoardsAwardsOverlay(EventBoardsAwardsOverlayMeta):
    itemsCache: Any
    __opener: Any
    __leaderboardID: Any
    def __init__(self):
        ...
    def setOpener(self, view):
        ...
    def changeFilter(self, lid):
        ...
    def _setData(self, lid):
        ...
    def _setVehicle(self, cd):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
