# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/account_completion_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.lobby.account_completion.tooltips.hangar_tooltip_view import HangarTooltipView as HangarTooltipView
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips import contexts as contexts
from gui.shared.tooltips.builders import TooltipWindowBuilder as TooltipWindowBuilder
__all__: tuple

class AccountCompletionTooltipData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, email=None, ownerViewID=None, *args, **kwargs):
        ...

def getTooltipBuilders():
    ...
