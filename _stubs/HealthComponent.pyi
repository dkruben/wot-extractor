# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/HealthComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from cgf_components_common.state_components import HealthComponentDescriptor as HealthComponentDescriptor
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from Event import Event as Event

# decorador original: @registerReplicableComponent
class HealthComponent(ReplicableDynamicScriptComponent, HealthComponentDescriptor):
    onHealthChanged: Any
    def __init__(self):
        ...
    def set_health(self, oldHealth):
        ...
