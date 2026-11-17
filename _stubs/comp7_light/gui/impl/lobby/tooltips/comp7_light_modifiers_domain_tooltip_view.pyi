# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/comp7_light_modifiers_domain_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider as ModifiersDataProvider
from battle_modifiers_ext.constants_ext import GameplayImpact as GameplayImpact
from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView as ModifiersDomainTooltipView
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN = 'comp7LightSeasonModifiers'

class Comp7LightModifiersDomainTooltipView(ModifiersDomainTooltipView):
    __comp7LightController: Any
    def getModifiersDataProvider(self):
        ...

class Comp7LightModifiersDataProvider(ModifiersDataProvider):
    @classmethod
    def isHiddenModifier(cls, mod):
        ...
    def _readClientDomain(self, modifier):
        ...
