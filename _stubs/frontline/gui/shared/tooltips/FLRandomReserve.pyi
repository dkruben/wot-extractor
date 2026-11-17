# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/shared/tooltips/FLRandomReserve.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import dependency as dependency, i18n as i18n
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from frontline_common.frontline_constants import FLBattleReservesModifier as FLBattleReservesModifier

class FLRandomReserve(BlocksTooltipData):
    __epicController: Any
    __sessionProvider: Any
    _NO_STACK_TOOLTIP_MIN_WIDTH = 315
    _STACK_TOOLTIP_MIN_WIDTH = 282
    _DISABLED_TOOLTIP_MIN_WIDTH = 244
    _RESERVES_OFFSET = 6
    USED_SLOT = 0
    itemCD: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    @staticmethod
    def __getR():
        ...
    @staticmethod
    def __getTitle(title):
        ...
    def __getSubTitle(self):
        ...
    @staticmethod
    def __getContent(content):
        ...
    def __getFooter(self, intCD):
        ...
    def __getDisabledBlocks(self):
        ...
    @staticmethod
    def __getEquipmentByIntCD(intCD):
        ...
    @staticmethod
    def __isPurchased(intCD):
        ...
    def __isDisabled(self, index):
        ...
    def __isUsed(self, item):
        ...
