# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/common_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.lobby.exchange.discount_info_tooltip_decorator import DiscountInfoTooltipContentWindowData as DiscountInfoTooltipContentWindowData, LimitedDiscountInfoTooltipContentWindowData as LimitedDiscountInfoTooltipContentWindowData
from gui.shared.tooltips import advanced as advanced, common as common, contexts as contexts, stronghold as stronghold
from gui.shared.tooltips.builders import AdvancedDataBuilder as AdvancedDataBuilder, DataBuilder as DataBuilder, DefaultFormatBuilder as DefaultFormatBuilder, TooltipWindowBuilder as TooltipWindowBuilder
from gui.shared.tooltips.dog_tags import DogTagInfoTooltip as DogTagInfoTooltip
from gui.shared.tooltips.filter import VehicleFilterTooltip as VehicleFilterTooltip
__all__: tuple

class HeaderMoneyAndXpBuilder(DataBuilder):
    __slots__: tuple
    __btnType: Any
    __hideActionBlock: Any
    def __init__(self, btnType, tooltipType, linkage, hideActionBlock=False):
        ...
    def _buildData(self, _advanced, *args, **kwargs):
        ...

class AdvancedHeaderMoneyAndXpBuilder(AdvancedDataBuilder):
    __slots__: tuple
    __btnType: Any
    __hideActionBlock: Any
    def __init__(self, btnType, tooltipType, linkage, hideActionBlock=False):
        ...
    def _buildData(self, _advanced, *args, **kwargs):
        ...

def getTooltipBuilders():
    ...
