# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/cgf_components/hexapod_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from cgf_script.registration import registerComponent as registerComponent
from GenericComponents import DynamicModelComponent as DynamicModelComponent, ParticleComponent as ParticleComponent, RemoveGoDelayedComponent as RemoveGoDelayedComponent
from Vehicular import HaxapodMovementLegComponent as HaxapodMovementLegComponent
from EdgeDrawer import EdgeHighlightComponent as EdgeHighlightComponent
from Sound import SoundObject3DComponent as SoundObject3DComponent
from cgf_components.highlight_component import HighlightComponent as HighlightComponent
from helpers.EffectMaterialCalculation import calcSurfaceMaterialNearPoint as calcSurfaceMaterialNearPoint
from material_kinds import EFFECT_MATERIALS as EFFECT_MATERIALS
from halloween_dyn_object_cache import getHexapodTerrainEffects as getHexapodTerrainEffects
_LEG_EFFECT_OBJ_NAME = 'hexapod_terrain_effect'
_UP_VECTOR: Any

class HWHexapodHighlight(object):
    colorIndex: Any
    def __init__(self, colorIndex=None):
        ...

# decorador original: @registerComponent
class HWIsHexapod(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'HW Is Hexapod'
    category = 'Halloween'

# decorador original: @registerComponent
class HWHexapodStepSoundComponent(object):
    domain = CGF.Domain.Client
    event: Any
    def __init__(self, event):
        ...

class HWHexapodSystem(CGF.System):
    VehicleHighlightActivated: Any
    VehicleHighlightDeactivated: Any
    HexapodActivated: Any
    HexapodLegActivated: Any
    HexapodLegDeactivated: Any
    HexapodDeactivated: Any
    HexapodHighlightActivated: Any
    HexapodStepSoundActivated: Any
    HexapodHighlightDeactivated: Any
    HighlightDeactivated: Any
    HighlightModelIterate: Any
    DynamicModelAccess: Any
    EdgeHighlightComponentAccess: Any
    Reactions: Any
    _hexapodGoByVehicleAppearance: Any
    _effects: Any
    _defaultEffect: Any
    def __init__(self):
        ...
    def _init(self):
        ...
    def update(self):
        ...
    def onEdgeHighlightComponentAdded(self, go, edgeHighlightComp, queue):
        ...
    def onHexapodComponentRemoved(self, go, queue, edgeHighlightComponentAccess):
        ...
    def onHexapodComponentAdded(self, go, queue, edgeHighlightComponentAccess):
        ...
    def onEdgeHighlightComponentRemoved(self, go, queue):
        ...
    def onHexapodHighlightAdded(self, go, hexapodHighlight, highlightComponent, dynamicModelAccess, highlightModelIterate):
        ...
    def onHexapodHighlightRemoved(self, go, highlightComponent, dynamicModelAccess, highlightModelIterate):
        ...
    def onHighlightComponentRemoved(self, highlightComponent, dynamicModelComponent, dynamicModelAccess):
        ...
    def _onLegMovementFinished(self, position):
        ...
    def __edgeDetectDynamicModel(self, enable, highlightComponent, dynamicModelComponent, dynamicModelAccess, colorIndex=None):
        ...
    def __enableGroupDraw(self, enable, go, groupName, dynamicModelAccess, highlightModelIterate, colorIndex=None):
        ...
    def onStepSoundAdded(self, hexapodStepSoundComponent, sound3dComponent):
        ...
