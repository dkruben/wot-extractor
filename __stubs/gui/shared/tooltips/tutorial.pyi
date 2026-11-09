# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/tutorial.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.RES_COMMON import RES_COMMON as RES_COMMON
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips import formatters as formatters
from gui.shared.formatters import text_styles as text_styles
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class HangarTutorialTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...

class HeaderPacker(HangarTutorialTooltipData):
    _title: Any
    _descr: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class CustomizationTypesPacker(HeaderPacker):
    _title: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class PersonalCaseSkillsPacker(HeaderPacker):
    _title: Any
    _descr: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class PersonalCaseFreeSkillsPacker(HeaderPacker):
    _title: Any
    _descr: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class PersonalCasePerksPacker(HeaderPacker):
    _title: Any
    _descr: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class PersonalCaseAdditionalPacker(HeaderPacker):
    _itemsCache: Any
    _title: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, tmanInvIdInList, *args, **kwargs):
        ...

class AmmunitionPacker(HeaderPacker):
    _title: Any
    _descr: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class EquipmentPacker(HeaderPacker):
    _title: Any
    _descr: Any
    def __init__(self, context):
        ...
