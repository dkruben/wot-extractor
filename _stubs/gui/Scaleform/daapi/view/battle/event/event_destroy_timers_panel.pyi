# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/event_destroy_timers_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.Scaleform.daapi.view.meta.EventDestroyTimersPanelMeta import EventDestroyTimersPanelMeta as EventDestroyTimersPanelMeta
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as BATTLE_NOTIFICATIONS_TIMER_TYPES
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as BATTLE_NOTIFICATIONS_TIMER_LINKAGES

class EventDestroyTimersPanel(EventDestroyTimersPanelMeta):
    __isVehOnFire: Any
    _vehicleInFireMessage: Any
    def __init__(self, mapping=None):
        ...
    def _generateMainTimersData(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def __setFireInVehicle(self, isInFire):
        ...
    def setVehicleInFireMessage(self, msg):
        ...
    def setWarningText(self, warningText, isInFire):
        ...
