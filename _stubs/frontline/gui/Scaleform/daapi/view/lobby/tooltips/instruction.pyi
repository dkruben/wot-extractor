# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/instruction.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from shared_utils import first as first
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import getOfferTokenByGift as getOfferTokenByGift
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_COMPONENT as TOOLTIP_COMPONENT, TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips.contexts import ToolTipContext as ToolTipContext
from helpers import dependency as dependency
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider

class EpicBattleTokenInstructionContext(ToolTipContext):
    __slots__: tuple
    __offersProvider: Any
    __hasOffer: Any
    def __init__(self):
        ...
    def buildItem(self, tokenID, **kwargs):
        ...

class EpicBattleInstructionTooltipData(BlocksTooltipData):
    _MAX_GIFTS_COUNT = 12
    def __init__(self, context):
        ...
    def _packBlocks(self, tokenID, **kwargs):
        ...
    @staticmethod
    def __packImageBlock(shortName):
        ...
    @classmethod
    def __packGiftNameBlocks(cls, shortName, giftsNames):
        ...
