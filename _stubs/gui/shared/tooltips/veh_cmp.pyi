# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/veh_cmp.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl import backport as backport
from gui.impl.gen import R as R

class VehCmpCustomizationTooltip(BlocksTooltipData):
    itemsCache: Any
    __vehicle: Any
    __camo: Any
    _customCamo: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args):
        ...
    def __packTitleBlock(self):
        ...
    def __packBonusBlock(self):
        ...
    def __packBottomPanelBlock(self):
        ...
