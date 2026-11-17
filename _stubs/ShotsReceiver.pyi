# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ShotsReceiver.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from cgf_components_common.material_component import MaterialComponent as MaterialComponent
from cgf_components.on_shot_components import EffectOnShotComponent as EffectOnShotComponent, SoundOnShotComponent as SoundOnShotComponent
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent
from Event import Event as Event
from material_kinds import EFFECT_MATERIAL_INDEXES_BY_IDS as EFFECT_MATERIAL_INDEXES_BY_IDS, EFFECT_MATERIAL_INDEXES_BY_NAMES as EFFECT_MATERIAL_INDEXES_BY_NAMES
_logger: Any
_DIR_UP: Any

# decorador original: @registerReplicableComponent
class ShotsReceiver(ReplicableDynamicScriptComponent):
    editorTitle = 'Shots Receiver'
    onShot: Any
    def __init__(self):
        ...
    def receiveShot(self, hitPoint, hitDir, speed, normal, shotID, effectIndex, prefabEffectIndex, shellType, shellCaliber, matKind, damagedDestructibles):
        ...

class ShotReceiverSystem(CGF.System):
    ShotActivated: Any
    ShotDeactivated: Any
    EffectAccess: Any
    SoundAccess: Any
    ExplosionAccess: Any
    MaterialAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __onShot(self, go, hitPoint, hitDir, speed, normal, shotID, effectIndex, prefabEffectIndex, shellType, shellCaliber, matKind, damagedDestructibles):
        ...
    def __processExplosion(self, gameObject, shot):
        ...
    def __processEffect(self, gameObject, shot, effectPath, transform):
        ...
    def __processSound(self, gameObject, shot, soundPath, transform):
        ...
