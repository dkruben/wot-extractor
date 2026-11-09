# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleBRStPatrickComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
import Event as Event
from debug_utils import LOG_DEBUG as LOG_DEBUG

class VehicleBRStPatrickComponent(DynamicScriptComponent):
    onCoinsAdded: Any
    def set_coinsCount(self, prev):
        ...
    def set_teammateCoinsCount(self, prev):
        ...
    @property
    def totalCoins(self):
        ...
    def __observedVehicleMatches(self):
        ...
