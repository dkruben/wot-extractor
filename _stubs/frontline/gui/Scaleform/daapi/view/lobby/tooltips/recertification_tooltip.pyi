# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/recertification_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_COMPONENT as TOOLTIP_COMPONENT, formatters as formatters
from gui.shared.tooltips.advanced import BaseAdvancedTooltip as BaseAdvancedTooltip
from gui.shared.tooltips.contexts import ToolTipContext as ToolTipContext
from gui.shared.tooltips.demount_kits import DemountKitToolTipData as DemountKitToolTipData
from helpers import dependency as dependency
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache

class EpicBattleBlanksContext(ToolTipContext):
    goodiesCache: Any
    def __init__(self, fieldsToExclude=None):
        ...
    def buildItem(self, recertificationFormID):
        ...

class EpicBattleRecertificationFormTooltipAdvanced(BaseAdvancedTooltip):
    def _packBlocks(self, *args, **kwargs):
        ...

class EpicBattleRecertificationFormTooltip(DemountKitToolTipData):
    _WIDTH = 400
    canIgnoreInventoryBlock: Any
    def __init__(self, context):
        ...
    def _packDescription(self):
        ...
