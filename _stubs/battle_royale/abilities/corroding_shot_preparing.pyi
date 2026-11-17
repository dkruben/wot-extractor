# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/corroding_shot_preparing.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from typing import List as List
import math_utils as math_utils
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
import GenericComponents as GenericComponents
from items import vehicles as vehicles
from battle_royale.abilities.common import getEffectSuffixForGunLength as getEffectSuffixForGunLength
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
_GUN_LENGTH_RANGES: dict
_GUN_EFFECT_OFFSET: dict

class VehicleCorrodingShotPreparingComponent(object):
    ...

class UpgradeInProgressComponent(object):
    ...

# decorador original: @registerComponent
class CorrodingShotPreparingComponent(object):
    editorTitle = 'Corroding Shot Preparing Component'
    group = 'Abilities'
    domain = CGF.Domain.Client
    gunNode: Any

# decorador original: @registerComponent
class CorrodingShotPreparingNodeComponent(object):
    editorTitle = 'Corroding Shot Preparing Node Component'
    group = 'Abilities'
    domain = CGF.Domain.Client
    effectPathTemplate: Any

class CorrodingShotPreparingSystem(CGF.System):
    __guiSessionProvider: Any
    VehicleShotActivated: Any
    BattleUpgradeDeactivated: Any
    VehicleShotDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def visualizeAbility(self, vehicleAbilityComponent):
        ...
    def __launch(self, vehicleAbilityComponent):
        ...
    def __setupVFX(self, nodeGO, vehicle, queue):
        ...
    def inBattleUpgradeCompleted(self, vehicleAbilityComponent):
        ...
    def stopVisualizeAbility(self, gameObject, queue):
        ...
