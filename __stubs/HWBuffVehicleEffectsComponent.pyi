# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffVehicleEffectsComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from HWBuffSequencesComponent import HWBuffSequencesComponent as HWBuffSequencesComponent
from dyn_components_groups import groupComponent as groupComponent
from xml_config_specs import StrParam as StrParam
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from constants import VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT

# decorador original: @groupComponent(...)
class HWBuffVehicleEffectsComponent(HWBuffSequencesComponent):
    _START_TRIGGER = 'start_trigger'
    _DEATH_MODULE = 'death'
    __isDeathModule: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def _onShowDamageFromShot(self, attackerID, points, effectsIndex, damageFactor, lastMaterialIsShield):
        ...
    def __onVehicleHealthChanged(self, _vehicleID, newHealth, oldHealth):
        ...
    def __onModelChanged(self):
        ...
