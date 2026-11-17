# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/discount_info_tooltip_decorator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.lobby.exchange.discount_info_tooltip import DiscountInfoTooltip as DiscountInfoTooltip, LimitedDiscountInfoTooltip as LimitedDiscountInfoTooltip
from gui.impl.lobby.exchange.exchange_rates_helper import NEED_ITEMS_TYPE_TO_EXCHANGE_RATE as NEED_ITEMS_TYPE_TO_EXCHANGE_RATE
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData

class DiscountInfoTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, needItemsType, *args, **kwargs):
        ...

class LimitedDiscountInfoTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, needItemsType, selectedExchangeAmount, *args, **kwargs):
        ...
