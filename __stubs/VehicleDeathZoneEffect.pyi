# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleDeathZoneEffect.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from death_zones_helpers import ZONE_STATE as ZONE_STATE
from constants import DEATH_ZONES as DEATH_ZONES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, DeathZoneTimerViewState as DeathZoneTimerViewState
from battle_royale.gui.battle_control.battle_constants import BrTimerViewState as BrTimerViewState
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class VehicleDeathZoneEffect(DynamicScriptComponent):
    guiSessionProvider: Any
    def _onAvatarReady(self):
        ...
    def set_state(self, _=None):
        ...
    def getTotalTime(self):
        ...
    def onDamaged(self):
        ...
