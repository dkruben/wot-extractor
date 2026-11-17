# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/cgf_components/loot_transparency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
import Triggers as Triggers
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME, CTRL_MODES as CTRL_MODES
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT

class PlayerAvatar(object):
    ...

# decorador original: @registerComponent
class LootSensorComponent(object):
    editorTitle = 'Loot Sensor'
    group = 'Steel Hunter'
    domain = CGF.Domain.Client
    trigger: Any
    enterReactionID: Any
    exitReactionID: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class LootTransparencyTriggerComponent(object):
    editorTitle = 'Loot Transparency Sensor'
    group = 'Steel Hunter'
    domain = CGF.Domain.Client
    modelMaterial: Any
    baseColor: Any
    alphaColor: Any
    baseOpacity: Any
    alphaOpacity: Any
    baseEmissionRate: Any
    alphaEmissionRate: Any
    particles: Any
    model: Any
    enterReactionID: Any
    exitReactionID: Any
    def __init__(self):
        ...

class LootSensorSystem(CGF.System):
    _LOOT_SENSOR_PREFAB = 'content/CGFPrefabs/steel_hunter/player_loot_sensor.prefab'
    _SENSOR_CTRL_MODES: tuple
    AvatarActivated: Any
    LootSensorActivated: Any
    LootSensorDeactivated: Any
    AreaTriggerAccess: Any
    DynamicModelAccess: Any
    ParticleAccess: Any
    TransparencyTriggerAccess: Any
    Reactions: Any
    def update(self):
        ...
    def onAvatarAdded(self, gameObject):
        ...
    def onAdded(self, lootSensor, triggerAccess):
        ...
    def onRemoved(self, lootSensor, triggerAccess):
        ...
    def __onEnter(self, who, _):
        ...
    def __onExit(self, who, _):
        ...
    def __changeParticleProperies(self, particle, opacity, emissionRate):
        ...
    def __changeModelMaterial(self, model, materialName, color):
        ...
