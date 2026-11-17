# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/boosters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.goodies.goodie_items import Booster as Booster, ClanReservePresenter as ClanReservePresenter
from gui.impl.backport import image as image, text as text
from gui.impl.common.personal_reserves.personal_reserves_shared_constants import PREMIUM_BOOSTER_IDS as PREMIUM_BOOSTER_IDS
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getTotalBoostersByResourceAndPremium as getTotalBoostersByResourceAndPremium
from gui.impl.gen import R as R
from gui.server_events import events_helpers as events_helpers
from gui.shared.formatters import text_styles as _ts
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData, CURRENCY_SETTINGS as CURRENCY_SETTINGS, makePriceBlock as makePriceBlock
from gui.shared.tooltips.contexts import BoosterInfoContext as BoosterInfoContext, BoosterStatsConfiguration as BoosterStatsConfiguration
from helpers import dependency as dependency
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, List as List, Optional as Optional
from gui.shared.items_cache import ItemsCache as ItemsCache
from gui.goodies import GoodiesCache as GoodiesCache
from gui.goodies.goodie_items import BoostersType as BoostersType

class BoosterTooltipData(BlocksTooltipData):
    itemsCache: Any
    goodiesCache: Any
    leftPadding: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, boosterID, *args, **kwargs):
        ...
    def __getHeader(self, booster):
        ...
    def __getInfoBlocks(self, booster, stats):
        ...
    def __getBonusBlocks(self, booster):
        ...
    def __getPriceInfo(self, stats, booster):
        ...
    def __getInDepot(self, booster):
        ...
    def __getReceiveBlock(self, booster):
        ...
    def __getActivationInfo(self, booster):
        ...
    def __packGrayText(self, message):
        ...
    def __getAccessCondition(self, questsResult):
        ...
    def __getActiveState(self, time):
        ...
    def __getBoosterQuestNames(self, boosterID):
        ...
