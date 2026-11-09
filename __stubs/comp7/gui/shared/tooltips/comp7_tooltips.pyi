# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/shared/tooltips/comp7_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from comp7.gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from comp7_common_const import offerRewardGiftToken as offerRewardGiftToken
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7_core.gui.shared.tooltips.comp7_core_tooltips import RoleSkillLobbyTooltipData as RoleSkillLobbyTooltipData, RoleSkillBattleTooltipData as RoleSkillBattleTooltipData
_logger: Any

class BattleResultsRatingPointsTooltip(BlocksTooltipData):
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *args):
        ...
    def __packHeaderBlock(self):
        ...
    def __packDescriptionBlock(self):
        ...

class BattleResultsTournamentRatingPointsTooltip(BlocksTooltipData):
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *args):
        ...
    def __packHeaderBlock(self):
        ...

class BattleResultsTrainingRatingPointsTooltip(BlocksTooltipData):
    def __init__(self, ctx):
        ...
    def _packBlocks(self, *args):
        ...
    def __packHeaderBlock(self):
        ...

class Comp7SelectableRewardTooltip(BlocksTooltipData):
    __offersProvider: Any
    _items: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, token, **kwargs):
        ...
    @staticmethod
    def __packImageBlock(giftTokenCategory):
        ...
    @staticmethod
    def __packRewardsBlock(tokenCategory):
        ...

class Comp7RoleSkillLobbyTooltipData(RoleSkillLobbyTooltipData):
    __comp7Controller: Any
    @property
    def _modeController(self):
        ...

class Comp7RoleSkillBattleTooltipData(RoleSkillBattleTooltipData):
    __comp7Controller: Any
    @property
    def _modeController(self):
        ...
