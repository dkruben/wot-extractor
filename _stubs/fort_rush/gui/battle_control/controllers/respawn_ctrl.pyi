# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_control/controllers/respawn_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from fort_rush.gui.fort_rush_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, VIEW_ALIAS as VIEW_ALIAS
from fort_rush.helpers.utils import retrievePlayerRespawnComponent as retrievePlayerRespawnComponent
from gui.app_loader import sf_battle as sf_battle
from gui.battle_control.arena_info.interfaces import ISpawnController as ISpawnController
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from helpers import dependency as dependency, uniprof as uniprof
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.shared import g_eventBus as g_eventBus
from event_platform.gui.shared.events import RespawnFrameworkEvent as RespawnFrameworkEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from typing import Dict as Dict, Optional as Optional, Union as Union
_logger: Any

class ISpawnListener(object):
    def setSpawnPoints(self, points):
        ...
    def showSpawnPoints(self):
        ...
    def closeSpawnPoints(self):
        ...
    def updatePoint(self, vehicleId, pointId, prevPointId):
        ...
    def updateCloseTime(self, timeLeft, state):
        ...
    def onSelectPoint(self, pointId):
        ...
    def setSpawnType(self, spawnType):
        ...

class FortRushRespawnViewController(ViewComponentsController, ISpawnController):
    _sessionProvider: Any
    __isSpawnPointsVisible: Any
    __invulnerableVehicleIDs: Any
    __respawnVehicleFilters: Any
    __eManager: Any
    onShowSpawnPoints: Any
    onCloseSpawnPoints: Any
    onChooseSpawnPoint: Any
    onTeamLivesUpdated: Any
    onTeamRespawnInfoUpdated: Any
    onTeamLivesSet: Any
    onVehicleInvulnerabilityChanged: Any
    __ingameMenu: Any
    def __init__(self):
        ...
    @property
    def isSpawnPointsVisible(self):
        ...
    def getRespawnVehicleFilters(self):
        ...
    def setRespawnVehicleFilters(self, filters):
        ...
    def getControllerID(self):
        ...
    def setVehicleInvulnerable(self, vehicleID, isInvulnerable):
        ...
    def isVehicleInvulnerable(self, vehicleID):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def setViewComponents(self, *components):
        ...
    def movingToRespawn(self):
        ...
    def showSpawnPoints(self, points=None):
        ...
    def updateSpawnPoints(self, points, pointGuid=None):
        ...
    def closeSpawnPoints(self, event=None):
        ...
    def chooseSpawnKeyPoint(self, pointId):
        ...
    def addRuntimeView(self, view):
        ...
    def removeRuntimeView(self, view):
        ...
    # decorador original: @sf_battle
    def _app(self):
        ...
    def __subscribeListeners(self):
        ...
    def __unsubscribeListeners(self):
        ...
    def __onViewAddedToContainer(self, _, pyEntity):
        ...
    def __onIngameMenuDisposed(self, _):
        ...
    def __onArenaPeriodChange(self, period, *_):
        ...
