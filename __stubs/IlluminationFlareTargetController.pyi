# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/IlluminationFlareTargetController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from helpers.dependency import descriptor as descriptor
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent

class IlluminationFlareTargetController(VehicleDynamicComponent):
    session: Any
    def __init__(self):
        ...
    def __onMarkersManagerMarkersCreated(self, event):
        ...
    def onDestroy(self):
        ...
    def set_spottedMarker(self, _):
        ...
    def __onVehicleControlling(self, _):
        ...
    def __update(self):
        ...
