# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/elen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.event_boards.event_boards_timer import FORMAT_MINUTE_STR as FORMAT_MINUTE_STR
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from gui.event_boards.event_boards_items import EVENT_DATE_TYPE as EVENT_DATE_TYPE
from gui.prb_control import prb_getters as prb_getters
from skeletons.gui.shared import IItemsCache as IItemsCache

class ElenPreviewTooltipData(BlocksTooltipData, IGlobalListener):
    _eventsController: Any
    _lobbyContext: Any
    _connectionMgr: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getHeader(self, currentEvent):
        ...
    def _getPrimeTimes(self, primeTimes):
        ...
    def _getBottom(self, currentEvent):
        ...

class BadgeTooltipData(BlocksTooltipData):
    __itemsCache: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, badgeID):
        ...

class BabgesGroupTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
