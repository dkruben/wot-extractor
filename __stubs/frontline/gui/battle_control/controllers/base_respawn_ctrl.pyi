# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/battle_control/controllers/base_respawn_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, defaultdict as defaultdict
import BigWorld as BigWorld
import Event as Event
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from gui.battle_control.avatar_getter import getSoundNotifications as getSoundNotifications
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from gui.veh_post_progression.battle_cooldown_manager import BattleCooldownManager as BattleCooldownManager
from helpers import dependency as dependency
from items import vehicles as vehicles
from post_progression_common import unpackVehSetupsIndexes as unpackVehSetupsIndexes
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IVehiclePostProgressionController as IVehiclePostProgressionController
from debug_utils import LOG_ERROR as LOG_ERROR
_Vehicle: Any
_RespawnInfo: Any
_RESPAWN_SOUND_ID = 'start_battle'
_SWITCH_SETUPS_ACTION = 0

class IRespawnView(object):
    def start(self, vehs, isLimited):
        ...
    def show(self, selectedID, vehs, cooldowns, limits=0):
        ...
    def hide(self):
        ...
    def updateTimer(self, timeLeft, vehs, cooldowns, limits=0):
        ...
    def setLimits(self, respawnLimits):
        ...
    def setBattleCtx(self, battleCtx):
        ...
    def setRespawnInfoExt(self, vehInfo, setupIndexes):
        ...

class BaseRespawnsController(ViewComponentsController):
    __slots__: tuple
    __postProgressionCtrl: Any
    __battleSession: Any
    showUiAllowed: Any
    respawnInfo: Any
    playerLives: Any
    vehicles: Any
    __isUIInited: Any
    __vehicles: Any
    __cooldowns: Any
    __limits: Any
    __respawnInfo: Any
    __timerCallback: Any
    __isUiShown: Any
    __isShowUiAllowed: Any
    __playerRespawnLives: Any
    __respawnSoundNotificationCallbackID: Any
    __respawnSoundNotificationRequest: Any
    __battleCtx: Any
    __setupsIndexes: Any
    __cooldownsManager: Any
    __eManager: Any
    onRespawnVisibilityChanged: Any
    onVehicleDeployed: Any
    onRespawnInfoUpdated: Any
    onPlayerRespawnLivesUpdated: Any
    onTeamRespawnLivesRestored: Any
    onRespawnVehiclesUpdated: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def setViewComponents(self, *components):
        ...
    def respawnPlayer(self):
        ...
    def chooseVehicleForRespawn(self, intCD):
        ...
    def sendSwitchVehSetupsLayout(self, vehCD, groupID, layoutIdx):
        ...
    def switchVehSetupsLayout(self, vehCD, groupID, layoutIdx):
        ...
    def movingToRespawn(self):
        ...
    def spawnVehicle(self, _):
        ...
    def updateRespawnVehicles(self, vehsList):
        ...
    def updateRespawnCooldowns(self, cooldowns):
        ...
    def updateRespawnInfo(self, respawnInfo):
        ...
    def updateVehicleLimits(self, respawnLimits):
        ...
    def updatePlayerRespawnLives(self, respawnLives):
        ...
    def restoredTeamRespawnLives(self, teams):
        ...
    def isRespawnVisible(self):
        ...
    def getLimits(self):
        ...
    def _show(self):
        ...
    def __setShowUiAllowed(self, value):
        ...
    def __clearRespawnSoundNotificationCallback(self):
        ...
    def __setRespawnSoundNotificationCallback(self):
        ...
    def __triggerRespawnSoundNotification(self):
        ...
    def __onRoundFinished(self, *args):
        ...
    def __refresh(self):
        ...
    def __hide(self):
        ...
    def __startTimer(self):
        ...
    def __stopTimer(self):
        ...
    def __updateRespawnInfoExt(self, intCD):
        ...
