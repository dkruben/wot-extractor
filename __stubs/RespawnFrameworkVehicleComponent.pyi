# wot-extractor: STUB (.pyi) gerado a partir de sources/res/event_platform/scripts/client/RespawnFrameworkVehicleComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import logging as logging
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from VehicleRespawnComponent import VehicleRespawnComponent as VehicleRespawnComponent
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control import avatar_getter as avatar_getter
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from event_platform.gui.shared.events import RespawnFrameworkEvent as RespawnFrameworkEvent
from event_platform_common.event_platform_constants import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from typing import List as List, Dict as Dict, Any as Any, Optional as Optional
_logger: _Any

class RespawnFrameworkVehicleComponent(VehicleRespawnComponent):
    _postmortem: _Any
    _selectedRespawnVehicleCD: _Any
    __spawnPoints: _Any
    def __init__(self):
        ...
    @property
    def spawnPoints(self):
        ...
    @property
    def isVehicleSelectionEnabled(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_respawnVehicles(self, _=None):
        ...
    def onDestroy(self):
        ...
    def onCameraChanged(self, controlModeName, vehicleID=None):
        ...
    def showPostmortem(self):
        ...
    def hidePostmortem(self):
        ...
    def __createPoints(self):
        ...
    def _getSelectedSetupsIndexes(self):
        ...
    def updateSelectedRespawnVehicle(self, vehicleCD):
        ...
    def __onArenaPeriodChange(self, period, *_):
        ...
