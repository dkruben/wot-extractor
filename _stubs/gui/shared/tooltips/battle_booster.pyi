# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/battle_booster.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES as SLOT_HIGHLIGHT_TYPES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import getKpiValueString as getKpiValueString
from gui.shared.tooltips import formatters as formatters, TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.module import PriceBlockConstructor as PriceBlockConstructor, InventoryBlockConstructor as InventoryBlockConstructor
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
_TOOLTIP_WIDTH = 468
_AUTOCANNON_SHOT_DISTANCE = 400
_MAX_INSTALLED_LIST_LEN = 10
_DEFAULT_PADDING = 20
_logger: Any

class BattleBoosterTooltipBlockConstructor(object):
    itemsCache: Any
    module: Any
    configuration: Any
    def __init__(self, module, configuration):
        ...
    def construct(self):
        ...

class HeaderBlockConstructor(BattleBoosterTooltipBlockConstructor):
    def construct(self):
        ...
    def _getOverlay(self):
        ...
    def _getIcon(self):
        ...

class EpicHeaderBlockConstructor(HeaderBlockConstructor):
    def _getOverlay(self):
        ...

class BattleBoosterBlockTooltipData(BlocksTooltipData):
    itemsCache: Any
    _headerBlockConstructor = HeaderBlockConstructor
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class EpicBattleBoosterBlockTooltipData(BattleBoosterBlockTooltipData):
    _headerBlockConstructor = EpicHeaderBlockConstructor

class BattleBoosterPriceBlockConstructor(PriceBlockConstructor):
    _priceLeftPadding: Any
    def __init__(self, module, configuration, valueWidth, leftPadding, rightPadding):
        ...

class BattleBoosterInventoryBlockConstructor(InventoryBlockConstructor):
    _inventoryPadding: Any
    def __init__(self, module, configuration, leftPadding, rightPadding):
        ...

class EffectsBlockConstructor(BattleBoosterTooltipBlockConstructor):
    def construct(self):
        ...
    @staticmethod
    def __getSkillTexts(skillLearnt, replaceText, boostText, applyStyles):
        ...

class BoosterHasNoEffectBlockConstructor(BattleBoosterTooltipBlockConstructor):
    def construct(self):
        ...
