# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/visual_effect_component_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Triggers as Triggers
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from account_helpers.settings_core.settings_constants import CONTOUR as CONTOUR
from cgf_components.highlight_component import HighlightComponent as HighlightComponent
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.components.component_constants import INVALID_EFFECT_INDEX as INVALID_EFFECT_INDEX
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes

class ImpactZoneComponent(object):
    segments: Any
    vehicleAppearance: Any
    maxComponentId: Any
    modelName: Any
    def __init__(self, segments, vehicleAppearance, maxComponentId):
        ...

class KillCamVisualEffectComponentSystem(CGF.System):
    __settingsCore: Any
    HighlightActivated: Any
    HighlightDeactivated: Any
    ModelAccess: Any
    ImpactZoneActivated: Any
    Reactions: Any
    def update(self):
        ...
    def __triggerReaction(self, go):
        ...
