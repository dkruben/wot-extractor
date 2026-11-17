# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/stronghold.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import getReserveNameVO as getReserveNameVO
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.items_parameters import params_helper as params_helper, formatters as paramsFormatters
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import int2roman as int2roman
from gui.prb_control.items.stronghold_items import StrongholdData as StrongholdData
_logger: Any

class StrongholdTooltipData(BlocksTooltipData):
    def _getEntity(self):
        ...
    def _getData(self):
        ...

class ReserveTooltipData(StrongholdTooltipData):
    BIG_ICON_SUFFIX = 'Big'
    BIG_GLOW_ICON_SUFFIX = 'BigGlow'
    LEVELS_WITHOUT_GLOW = 10
    def __init__(self, context):
        ...
    def _packBlocks(self, *args):
        ...
    def __getHeaderBlock(self, item, name, level, count, isPlayerLegionary):
        ...
    def __getMainParamsBlock(self, name, item):
        ...
    def __getAdditionalParamsBlock(self, reserve):
        ...
    def __packParameterBlock(self, name, value, measureUnits):
        ...
    def __getReserveIconName(self, name, level):
        ...
