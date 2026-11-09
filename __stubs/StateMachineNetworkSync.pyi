# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StateMachineNetworkSync.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from CgfStateMachine import StateMachineComponent as StateMachineComponent

# decorador original: @registerReplicableComponent
class StateMachineNetworkSync(ReplicableDynamicScriptComponent):
    editorTitle = 'CGF State Machine Network Sync'

class StateMachineNetworkSyncSystem(CGF.System):
    StateMachineIterate: Any
    Reactions: Any
    def update(self):
        ...
