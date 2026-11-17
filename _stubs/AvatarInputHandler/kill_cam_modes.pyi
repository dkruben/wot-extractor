# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/kill_cam_modes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import weakref as weakref
import typing as typing
import BigWorld as BigWorld
import constants as constants
import Keys as Keys
import Math as Math
import BattleReplay as BattleReplay
import math_utils as math_utils
import GUI as GUI
import CommandMapping as CM
from PlayerEvents import g_playerEvents as g_playerEvents
from battleground.simulated_scene import SimulatedScene as SimulatedScene, ANIMATION_DURATION_BEFORE_SHOT as ANIMATION_DURATION_BEFORE_SHOT
from constants import ATTACK_REASON as ATTACK_REASON, ATTACK_REASONS as ATTACK_REASONS, ARENA_PERIOD as ARENA_PERIOD, DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX, POSTMORTEM_MODIFIERS as POSTMORTEM_MODIFIERS
from gui.battle_control.arena_info.interfaces import IBattleFieldController as IBattleFieldController
from gui.shared.events import DeathCamEvent as DeathCamEvent
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from wotdecorators import noexcept as noexcept
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera as ArcadeCamera
from AvatarInputHandler.DynamicCameras.kill_cam_camera import KillCamera as KillCamera, StartCamDirection as StartCamDirection, LOOK_AT_KILLER_DURATION as LOOK_AT_KILLER_DURATION
from AvatarInputHandler.control_modes import IControlMode as IControlMode, _readCameraTransitionSettings as _readCameraTransitionSettings
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from helpers import dependency as dependency, uniprof as uniprof
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from AvatarInputHandler.PostmortemDelay import PostmortemDelay as PostmortemDelay
from account_helpers.AccountSettings import AccountSettings as AccountSettings, WHEELED_DEATH_DELAY_COUNT as WHEELED_DEATH_DELAY_COUNT
from typing import Dict as Dict, Any as Any
_PARTICLES_DURATION_AFTER_SHOT = 0.0
_PREPARE_KILLER_VISION_FADE_TIME = 0.8
_SHOW_KILLER_VISION_FADE_TIME = 1.0
_LEAVE_KILLER_VISION_FADE_TIME = 0.8
_SHOW_DEAD_TANK_FADE_TIME = 1.0
_START_VISION_DELAY = 1.0
_KILL_CAM_WAIT_TIME = 2.0
_TIME_BEFORE_FOLLOW_TANK = 2.0
_WHEELED_VEHICLE_POSTMORTEM_DELAY = 3.0
_LOOK_AT_KILLER_DURATION_LEGACY = 2.0
_LOOK_AT_KILLER_SUBSTITUTE_WAIT_TIME = 5
_NO_SKIP_DEATH_CAM_DURATION = 2.0
_PAUSE_BUTTON_COOLDOWN = 0.5
_SKIP_KILL_CAM_BEFORE_AUTORESPAWN_TIME = 15
_RADIUS = 10
_RADIUS_ALPHA = 2
_BLOCKED_KEYS: set
_BLOCKED_ACTIONS: tuple
_BLACK_BG_IMG = 'gui/maps/login/blackBg.png'
_logger: _Any

class SimulationAvailability(object):
    AVAILABLE = 0
    NOT_AVAILABLE_MISSING_DATA = 1
    NOT_AVAILABLE_END_OF_BATTLE = 2
    VEHICLES_TOO_CLOSE = 3
    NOT_KILLED_BY_SHOT = 4
    NOT_SUPPORTED_MODE = 5
    NOT_ENOUGH_TIME = 6
    NOT_AVAILABLE: tuple

class KillModeBase(IControlMode, CallbackDelayer):
    guiSessionProvider: _Any
    _modeEnteredTime: _Any
    _victimVehicleID: _Any
    _killerVehicleID: _Any
    _rawSimulationData: _Any
    _trajectoryPoints: _Any
    _postmortemKwargs: _Any
    _skipBattleTimeLeft: _Any
    _cameraTransitionDurations: _Any
    _aih: _Any
    _cam: _Any
    __killCamState: _Any
    def __init__(self, dataSection, avatarInputHandler):
        ...
    @property
    def camera(self):
        ...
    @property
    def curVehicleID(self):
        ...
    @property
    def killCamCtrl(self):
        ...
    @property
    def killCamState(self):
        ...
    @property
    def _killerIsSpotted(self):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def enable(self, **kwargs):
        ...
    def disable(self, smoothFade=True):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def _leaveMode(self):
        ...
    def _handleModeExecution(self):
        ...
    def _changeKillCamModeState(self, newState):
        ...
    def _canShowKillerVisionInPeriod(self):
        ...
    def _areBothTeamsAlive(self):
        ...
    def _checkSimulationAvailability(self):
        ...
    def _validateRawSimulationData(self, rawSimulationData):
        ...
    def _canSkipKillCamera(self):
        ...
    def _canSwitchToFreecam(self):
        ...
    def _canSwitchToAllyVehicle(self):
        ...
    def _switchToCtrlMode(self, targetMode, **kwargs):
        ...
    def _isKillByShot(self):
        ...
    def _isFirstTenDeathsWheeledTank(self, vehicleID):
        ...
    def _tryDecrementWheeledDeathCounter(self, vehicleID):
        ...
    def __getRawSimulationData(self, vehicle):
        ...
    def __onReceiveKillerID(self, vehicleID):
        ...

class KillCamMode(KillModeBase):
    __isLeaveKillCamWhenPrepared: _Any
    __bFadeScreenActive: _Any
    __lastTimePauseToggled: _Any
    __vehicleRespawnTriggered: _Any
    __isAutoRespawnScheduled: _Any
    __simulatedVictimID: _Any
    __simulatedKillerID: _Any
    __unspottedOrigin: _Any
    __simulatedScene: _Any
    __skipKillCamDistance: _Any
    _skipBattleTimeLeft: _Any
    _skipNotEnoughTimeForDC: _Any
    _rawSimulationData: _Any
    _trajectoryPoints: _Any
    def __init__(self, dataSection, avatarInputHandler):
        ...
    @property
    def __isRicochet(self):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def enable(self, **kwargs):
        ...
    def disable(self, smoothFade=True):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def handleReplayKeyEvent(self, isDown, key):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def isSelfVehicle(self):
        ...
    def togglePauseKillCam(self):
        ...
    def _handleModeExecution(self):
        ...
    # decorador original: @noexcept
    def _leaveMode(self):
        ...
    def _canSkipKillCamera(self):
        ...
    def _switchToCtrlMode(self, targetMode, **kwargs):
        ...
    def _checkSimulationAvailability(self):
        ...
    def _validateRawSimulationData(self, rawSimulationData):
        ...
    def __onSwitchToPostmortem(self, noRespawnPossible, respawnAvailable):
        ...
    def __initializeSimulationData(self):
        ...
    def __skipKillCam(self, simulationAvailability):
        ...
    def __fadeAndPrepareKillCamData(self):
        ...
    def __prepareAnimationsAndCam(self):
        ...
    def __onAllVehiclesLoaded(self):
        ...
    def __startKillCamSimulation(self):
        ...
    def __notifyKillCamCtrl(self):
        ...
    def __fadeScreen(self, bFade=True, duration=1.0):
        ...
    def __startScreenFade(self, isFadeToBlack, duration):
        ...
    def __startBlackScreen(self, isFadeToBlack, duration):
        ...
    def __setBlackScreen(self, isFadeToBlack):
        ...
    def __enableEdgeDrawing(self):
        ...
    def __fadeAndLeaveKillCam(self, isInterrupted=False):
        ...
    def __simulatedSceneEnded(self):
        ...
    def __displayKillCamAnimationEffects(self):
        ...
    def __stopParticlesAfterShot(self):
        ...
    def __pauseResumeChanged(self, pause):
        ...
    def __onVehicleAnimationFinished(self):
        ...
    def __onArenaPeriodChanged(self, period, *args):
        ...
    def __onRespawnInfoUpdate(self, respawnInfo):
        ...
    def __onVehicleRespawn(self):
        ...
    def __forceExitKillCamScene(self):
        ...
    def __isDistanceFarEnough(self, simulationData):
        ...

class LookAtKillerMode(KillModeBase):
    _rawSimulationData: _Any
    _trajectoryPoints: _Any
    def _handleModeExecution(self):
        ...
    def _leaveMode(self):
        ...
    def __handleLookAtKillerFlow(self):
        ...
    def __startCameraRotation(self, simAvailability):
        ...
    def __handleCameraRotation(self, enemySpottedInsideAOI=False, killerIsSpotted=False):
        ...
