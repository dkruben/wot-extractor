# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/demount_kits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.goodies.goodie_items import DemountKit as DemountKit
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, _logger as _logger
from gui.shared.money import Currency as Currency
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.wgm_currency import WGMCurrencyTooltip as WGMCurrencyTooltip
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class GoldToolTipData(BlocksTooltipData):
    _itemsCache: Any
    _WIDTH = 320
    _TOP = 17
    _LEFT = 20
    _BOTTOM = 18
    _RIGHT = 13
    _ICON_Y_OFFSET = 2
    _LEFT_PADDING = 20
    _btnType: Any
    def __init__(self, ctx):
        ...
    def _packBlocks(self, btnType=None, *args, **kwargs):
        ...

class GoldStatsToolTipData(WGMCurrencyTooltip):
    def _getAlternativeData(self):
        ...

class DemountKitToolTipData(BlocksTooltipData):
    _WIDTH = 320
    canIgnoreInventoryBlock: Any
    _item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _packHeader(self):
        ...
    def _packDescription(self):
        ...
    def _packInventoryBlock(self):
        ...

class NotEnoughMoneyTooltipData(ToolTipBaseData):
    RESOURCES_BY_CURRENCY: dict
    def __init__(self, context):
        ...
    def getDisplayableData(self, value, currencyType):
        ...
