# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/area_abilities.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Math as Math
from battle_royale.abilities.adaptation_restore_health import AdaptationHealthRestoreEffectArea as AdaptationHealthRestoreEffectArea
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from battle_royale_artefacts import ThunderStrike as ThunderStrike, ZonesCircle as ZonesCircle

# decorador original: @registerComponent
class AreaAbilityVisualizer(object):
    editorTitle = 'Area Ability Visualizer'
    group = 'Abilities'
    domain = CGF.Domain.ClientEditor
    areaTransform: Any
    manualRadius: Any
    def __init__(self):
        ...

class AreaAbilityVisualizationSystem(CGF.System):
    VisualizerActivated: Any
    ThunderStrikeActivated: Any
    ZonesCircleActivated: Any
    HealthRestoreActivated: Any
    TransformAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __applyScale(self, transformComponent, radius):
        ...
    def __resizeVisualizer(self, visualizer, radius, transformAccess):
        ...
    def checkManualRadius(self, visualizer, transformAccess):
        ...
    def resizeThunderTransform(self, visualizer, thunderStrike, transformAccess):
        ...
    def resizeZonesCircle(self, visualizer, zonesCircle, transformAccess):
        ...
    def resizeHealthRestoreAbilityCircle(self, visualizer, area, transformAccess):
        ...
