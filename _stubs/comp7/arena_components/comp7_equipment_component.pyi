# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/arena_components/comp7_equipment_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.arena_components.comp7_core_equipment_component import Comp7CoreEquipmentComponent as Comp7CoreEquipmentComponent, _AoeHealEffect as _AoeHealEffect
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class _Comp7AoeHealEffect(_AoeHealEffect):
    __comp7Controller: Any
    @property
    def _modeController(self):
        ...

class Comp7EquipmentComponent(Comp7CoreEquipmentComponent):
    _AOE_HEAL_EFFECT = _Comp7AoeHealEffect
