# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/shared/tooltips/battle_royale_modules.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.common.battle_royale.params import getModuleParameters as getModuleParameters, getVehicleParameters as getVehicleParameters
from gui.Scaleform.genConsts.ATLAS_CONSTANTS import ATLAS_CONSTANTS as ATLAS_CONSTANTS
from gui.doc_loaders.battle_royale_settings_loader import getTreeModuleIcon as getTreeModuleIcon, getTreeModuleHeader as getTreeModuleHeader
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
_TOOLTIP_MIN_WIDTH = 410

class BattleRoyaleModulesTooltip(BlocksTooltipData):
    item: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    def _getVehicle(self):
        ...

class HeaderBlockConstructor(object):
    @classmethod
    def construct(cls, module):
        ...
    @classmethod
    def __constructModule(cls, module):
        ...
    @classmethod
    def __constructVehicle(cls, vehicle):
        ...

class ParamsBlockConstructor(object):
    @staticmethod
    def construct(module, currentModule, vehicle):
        ...
