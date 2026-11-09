# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/battle_pass.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_pass_common import BattlePassState as BattlePassState
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class BattlePassGiftTokenTooltipData(BlocksTooltipData):
    _MAX_GIFTS_COUNT = 12
    def __init__(self, context):
        ...
    def _packBlocks(self, tokenID, isReceived=False, **kwargs):
        ...
    @staticmethod
    def __packFooterBlock(shortName):
        ...
    @staticmethod
    def __packImageBlock(shortName):
        ...
    @classmethod
    def __packGiftNameBlocks(cls, shortName, giftsNames, isOfferEnabled):
        ...

class BattlePassPointsTooltipData(BlocksTooltipData):
    __battlePassController: Any
    _items: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
