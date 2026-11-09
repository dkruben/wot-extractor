# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/tooltips/comp7_core_modifiers_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_modifiers.gui.impl.lobby.feature.helpers import packModifierModel as packModifierModel
from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView as ModifiersDomainTooltipView
from comp7_core.gui.impl.gen.view_models.views.lobby.tooltips.modifiers_tooltip.modifiers_tooltip_model import ModifiersTooltipModel as ModifiersTooltipModel
from comp7_core.gui.impl.gen.view_models.views.lobby.tooltips.modifiers_tooltip.sub_mode_modifiers import SubModeModifiers as SubModeModifiers
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_modifiers_data_provider import Comp7CoreSubModifiers as Comp7CoreSubModifiers, Comp7CoreModifiersDataProvider as Comp7CoreModifiersDataProvider
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7CoreModifiersTooltipView(ModifiersDomainTooltipView):
    __comp7Controller: Any
    __slots__: tuple
    __subModesProvider: Any
    def __init__(self, modifiersDomain):
        ...
    def getModifiersDataProvider(self):
        ...
    def _invalidateSubModes(self, model):
        ...
