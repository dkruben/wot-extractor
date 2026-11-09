# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.Scaleform.daapi.view.meta.EventPlayersPanelMeta import EventPlayersPanelMeta as EventPlayersPanelMeta
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.shared.badges import buildBadge as buildBadge
from PlayerEvents import g_playerEvents as g_playerEvents

class EventPlayersPanel(EventPlayersPanelMeta, IArenaVehiclesController):
    sessionProvider: Any
    _points: Any
    __arenaDP: Any
    def __init__(self):
        ...
    def invalidateVehiclesInfo(self, _):
        ...
    def invalidateArenaInfo(self):
        ...
    def addVehicleInfo(self, vo, _):
        ...
    def updateVehiclesInfo(self, updated, arenaDP):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def __updateAllTeammates(self):
        ...
    def __updateTeammate(self, vInfo, hpCurrent):
        ...
    def setPoints(self, vehID, points):
        ...
    def getPoints(self, vehID):
        ...
