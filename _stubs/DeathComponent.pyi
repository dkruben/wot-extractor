# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/DeathComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
from cgf_components_common.state_components import DeathComponentDescriptor as DeathComponentDescriptor, SpawnOnDeathComponent as SpawnOnDeathComponent, RemoveOnDeathComponent as RemoveOnDeathComponent
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from cgf_components.on_death_components import SoundOnDeathComponent as SoundOnDeathComponent, EffectOnDeathComponent as EffectOnDeathComponent, ChangeModelOnDeathComponent as ChangeModelOnDeathComponent
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from functools import partial as partial

# decorador original: @registerReplicableComponent
class DeathComponent(ReplicableDynamicScriptComponent, DeathComponentDescriptor):
    ...

class DeathComponentSystem(CGF.System):
    RemoveOnDeathActivated: Any
    SpawnOnDeathActivated: Any
    SoundOnDeathComponentActivated: Any
    EffectOnDeathComponentActivated: Any
    ChangeModelOnDeathComponentActivated: Any
    ChangeModelOnDeathComponentDeactivated: Any
    Reactions: Any
    def update(self):
        ...

def removeGameObject(go):
    ...
def loadPrefab(prefabPath, go, tr, loadIntoHierarchy):
    ...
def changeModel(go, modelPath, spaceID):
    ...
