# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/tooltips/modifiers_domain_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from battle_modifiers.gui.impl.lobby.feature.helpers import packModifierModel as packModifierModel
from battle_modifiers.gui.impl.gen.view_models.views.lobby.tooltips.modifiers_domain_tooltip_view_model import ModifiersDomainTooltipViewModel as ModifiersDomainTooltipViewModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from battle_modifiers.gui.feature.modifiers_data_provider import ModifiersDataProvider as ModifiersDataProvider

class ModifiersDomainTooltipView(ViewImpl):
    __slots__: tuple
    _modifiersDomain: Any
    def __init__(self, modifiersDomain, layoutID=..., model=None, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @property
    def viewModel(self):
        ...
    def getModifiersDataProvider(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __invalidateModifiers(self, modifiers):
        ...
    def _invalidateSubModes(self, model):
        ...
