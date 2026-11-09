# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VehicleRespawnComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
from constants import RespawnState as RespawnState, VEHICLE_SETTING as VEHICLE_SETTING, IS_VS_EDITOR as IS_VS_EDITOR
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from shared_utils import nextTick as nextTick
from helpers.EffectsList import RespawnDestroyEffect as RespawnDestroyEffect

class VehicleRespawnComponent(DynamicScriptComponent):
    onVehicleRespawned: Any
    onSetSpawnTime: Any
    guiSessionProvider: Any
    def onDestroy(self):
        ...
    def chooseSpawnGroup(self, groupName):
        ...
    def set_spawnTime(self, prev):
        ...
    def set_respawnState(self, prev):
        ...
    def waitForRespawnReadiness(self):
        ...
    def _respawnVehicle(self):
        ...
    def _onVehicleAppeared(self):
        ...
    def _explodeVehicleBeforeRespawn(self):
        ...
