# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/crest_moving_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import CGF as CGF
from cgf_common.cgf_helpers import getVehicleEntityByVehicleGameObject as getVehicleEntityByVehicleGameObject
from cgf_components.crest_moving_effects_component import CrestMovingEffectsComponent as CrestMovingEffectsComponent
from constants import CREST_MOVING_STATE as CREST_MOVING_STATE
from gui.battle_control.controllers.vehicles_tracking import VehiclesTrackingWatcher as VehiclesTrackingWatcher
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from CrestMovingController import CrestMovingState as CrestMovingState
_logger: Any

class CrestMovingEffectsSystem(CGF.System, VehiclesTrackingWatcher):
    EffectsActivated: Any
    EffectsDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def __onStateChanged(self, effectsComponent, previousState, newState):
        ...
    def __startMoving(self, effectsComponent, state):
        ...
    def __stopActiveSound(self, effectsComponent):
        ...
