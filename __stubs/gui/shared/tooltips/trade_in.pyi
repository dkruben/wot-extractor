# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/trade_in.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.time_formatters import getDueDateOrTimeStr as getDueDateOrTimeStr
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.server_events import IEventsCache as IEventsCache

class TradeInInfoTooltipData(BlocksTooltipData):
    __eventsCache: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    @staticmethod
    def __getHeader():
        ...
    @staticmethod
    def __getInfo():
        ...
    @staticmethod
    def __getFooter():
        ...

class TradeInInfoNotAvailableData(ToolTipBaseData):
    __tradeIn: Any
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class TradeInStateNotAvailableData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _withTradeInUntil(tradeIn=None):
    ...
