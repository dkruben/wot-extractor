# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TestReplicableComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GenericComponents as GenericComponents
import GameplayDebug as GameplayDebug
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from cgf_demo.test_replicable import TestReplicableComponentDescriptor as TestReplicableComponentDescriptor
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from Event import Event as Event

# decorador original: @registerReplicableComponent
class TestReplicableComponent(ReplicableDynamicScriptComponent, TestReplicableComponentDescriptor):
    onReplicated: Any
    def __init__(self):
        ...
    def set_replicableInt(self, old):
        ...
    def set_replicableFloat(self, old):
        ...
    def set_replicableString(self, old):
        ...
    def set_replicableVector3(self, old):
        ...
    def set_replicableStringList(self, old):
        ...

class DisplayReplicableValuesSystem(CGF.System):
    ReplicableAdded: Any
    ReplicableIterate: Any
    Reactions: Any
    totalReplicationCount: Any
    def __init__(self):
        ...
    def update(self):
        ...
    def __onReplicationDone(self, prev, new):
        ...
