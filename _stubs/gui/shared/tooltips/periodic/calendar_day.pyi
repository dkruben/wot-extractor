# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/periodic/calendar_day.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import time_utils as time_utils
from items.writers.c11n_writers import natsorted as natsorted
_CONTENT_MARGINS: dict
_TOOLTIP_MARGIN = 13
_TOOLTIP_MIN_WIDTH = 200

class PeriodicCalendarDayTooltip(BlocksTooltipData):
    _RES_ROOT = None
    _TOOLTIP_TYPE = None
    def __init__(self, ctx):
        ...
    def _getController(self, *_):
        ...
    def _isValidPrimeTimes(self, _):
        ...
    def _packBlocks(self, *args):
        ...
    def _packHeaderBlock(self):
        ...
    def __packServerTimeBlock(self, serverStr, timeStr):
        ...
