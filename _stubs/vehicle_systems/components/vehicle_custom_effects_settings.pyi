# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicle_custom_effects_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Vehicular as Vehicular
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CGF_DUMP as IS_CGF_DUMP

class CustomEffectManager(object):
    ...

# decorador original: @registerComponent
class VehicleCustomEffectsSettings(object):
    domain = CGF.Domain.Client
    category = 'Vehicle'
    editorTitle = 'Vehicle Custom Effects Settings'
    disableDefaultChassis: Any
    disableDefaultHull: Any
    additionalEngineSoundPC: Any
    additionalEngineSoundNPC: Any

class VehicleCustomEffectsSystem(CGF.System):
    VehicleCustomEffectsSettings: Any
    CustomEffectManagerAccess: Any
    AuditionAccess: Any
    Reactions: Any
    def update(self):
        ...
