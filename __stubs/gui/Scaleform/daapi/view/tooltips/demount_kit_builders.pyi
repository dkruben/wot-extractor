# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/demount_kit_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts as contexts, advanced as advanced, demount_kits as demount_kits
from gui.shared.tooltips.builders import AdvancedDataBuilder as AdvancedDataBuilder, DefaultFormatBuilder as DefaultFormatBuilder
__all__: tuple

class AlternativeGoldTooltipBuilder(AdvancedDataBuilder):
    __slots__: tuple
    __btnType: Any
    def __init__(self, tooltipType, linkage, provider, adProvider):
        ...
    def _buildData(self, _advanced, *args, **kwargs):
        ...

def getTooltipBuilders():
    ...
