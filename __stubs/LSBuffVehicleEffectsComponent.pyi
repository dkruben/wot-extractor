# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSBuffVehicleEffectsComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from LSBuffSequencesComponent import LSBuffSequencesComponent as LSBuffSequencesComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from dyn_components_groups import groupComponent as groupComponent
from xml_config_specs import StrParam as StrParam
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from constants import VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT

# decorador original: @groupComponent(...)
class LSBuffVehicleEffectsComponent(LSBuffSequencesComponent):
    _guiSessionProvider: Any
    _START_TRIGGER = 'start_trigger'
    _DEATH_MODULE = 'death'
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def _onShowDamageFromShot(self, attackerID, points, effectsIndex, damageFactor, lastMaterialIsShield):
        ...
    def _onVehicleKilled(self, victimID, *_):
        ...
