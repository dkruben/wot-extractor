# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/tooltips/vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.vehicle import StatusBlockConstructor as StatusBlockConstructor
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
_TOOLTIP_WIDTH = 420

class VehicleTooltipData(BlocksTooltipData):
    __battleRoyaleController: Any
    def __init__(self, context=None):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def __constructStatusBlock(self, vehicle):
        ...
    @classmethod
    def __constructHeaderBlock(cls, vehicle):
        ...
    @staticmethod
    def __constructDescriptionBlock(vehicle):
        ...
    @staticmethod
    def __setBackground(vehicle):
        ...
