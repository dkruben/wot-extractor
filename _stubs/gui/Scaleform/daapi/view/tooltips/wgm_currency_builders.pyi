# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/wgm_currency_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts as contexts
from gui.shared.tooltips import wgm_currency as wgm_currency
from gui.shared.tooltips.builders import DataBuilder as DataBuilder
__all__: tuple

class CurrencyTooltipBuilder(DataBuilder):
    __slots__: tuple
    __btnType: Any
    __hideActionBlock: Any
    def __init__(self, btnType, tooltipType, linkage, hideActionBlock=False):
        ...
    def _buildData(self, advanced, *args):
        ...

def getTooltipBuilders():
    ...
