# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TargetDesignatorTargetController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import DIRECT_DETECTION_TYPE as DIRECT_DETECTION_TYPE
from gui.battle_control.avatar_getter import isFPV as isFPV, getVehicleIDAttached as getVehicleIDAttached
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from helpers.dependency import descriptor as descriptor
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager as MarkersManager
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin as VehicleMarkerPlugin

class TargetDesignatorTargetController(VehicleDynamicComponent):
    session: Any
    isFPV: Any
    def __init__(self):
        ...
    def __onMarkersManagerMarkersCreated(self, event):
        ...
    def onDestroy(self):
        ...
    def set_spottedMarker(self, _):
        ...
    def set_hasUnspottedIndicator(self, _):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def __onVehicleControlling(self, _):
        ...
    def __update(self):
        ...
