# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/settings_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_model import PerkType as PerkType
from gui.Scaleform.daapi.view.tooltips.tankman_builders import CrewPerkTooltipData as CrewPerkTooltipData
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts as contexts
from gui.shared.tooltips import common as common
from gui.shared.tooltips.builders import DataBuilder as DataBuilder, DefaultFormatBuilder as DefaultFormatBuilder, TooltipWindowBuilder as TooltipWindowBuilder
__all__: tuple

class SituationalPerkTooltipData(CrewPerkTooltipData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, skillName, *args, **kwargs):
        ...

def getTooltipBuilders():
    ...
