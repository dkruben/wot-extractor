# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/referral_program/awards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import lookupItem as lookupItem, getCDFromId as getCDFromId, getItemIcon as getItemIcon, getItemTitle as getItemTitle
from web.web_client_api.common import ItemPackEntry as ItemPackEntry, ItemPackType as ItemPackType, ItemPackTypeGroup as ItemPackTypeGroup
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
_logger: Any
_ICON_SIZE = '48x48'

class AwardsTooltipData(BlocksTooltipData):
    _TOOLTIP_MIN_WIDTH = 340
    __itemsCache: Any
    __goodiesCache: Any
    __resPath = R.strings.tooltips.referralProgram.newLevelAwards
    __shieldStatus: Any
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __packHeader(self):
        ...
    def __packItemBlock(self, items):
        ...
    def __getItemData(self, itemType, itemId):
        ...
    def __getCustomization(self, rawItem, itemId):
        ...
    def __getDemountKit(self, itemId):
        ...
