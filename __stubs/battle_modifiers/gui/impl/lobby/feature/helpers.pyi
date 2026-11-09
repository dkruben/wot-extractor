# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/feature/helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional
from battle_modifiers.gui.impl.lobby.feature.constants import MOD_TYPE_MAP as MOD_TYPE_MAP, PHYS_TYPE_MAP as PHYS_TYPE_MAP, USE_TYPE_MAP as USE_TYPE_MAP, GAMEPLAY_IMPACT_MAP as GAMEPLAY_IMPACT_MAP
from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.modifier_model import ModifierModel as ModifierModel
from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.limit_model import LimitModel as LimitModel, LimitType as LimitType
from battle_modifiers_ext.battle_modifiers import ModifierBase as ModifierBase
from frameworks.wulf import Array as Array

def packModifierModel(modifier):
    ...
def _invalidateLimits(modifier, limitsModel):
    ...
def _packLimitModel(value, limitType):
    ...
