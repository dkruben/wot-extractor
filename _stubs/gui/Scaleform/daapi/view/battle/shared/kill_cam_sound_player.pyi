# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/kill_cam_sound_player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
import BigWorld as BigWorld
from AvatarInputHandler.DynamicCameras.kill_cam_camera import CallbackPauseManager as CallbackPauseManager
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.kill_cam_ctrl import KillCamInfoMarkerType as KillCamInfoMarkerType, DistanceMarkerData as DistanceMarkerData
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from gui.shared.events import DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_TRAJECTORY_PROGRESS_DELAY = 0.1

class _DeathCamSound(object):
    DC_WW_RTPC_ext_dc_trajectory_progress = 'RTPC_ext_dc_trajectory_progress'
    DC_WW_STATE_GROUP = 'STATE_deathcam'
    DC_WW_STATE_ON = 'STATE_deathcam_on'
    DC_WW_STATE_OFF = 'STATE_deathcam_off'
    DC_MUTE_GAME_AUDIO: dict
    DC_SIMULATED_SCENE_ENTER = 'dc_simulated_scene_enter'
    DC_SIMULATED_SCENE_EXIT = 'dc_simulated_scene_exit'
    DC_AMBIENT_START = 'dc_amb_start'
    DC_AMBIENT_STOP = 'dc_amb_stop'
    DC_TRAJECTORY_RAY = 'dc_trajectory_ray'
    DC_TRANSITION_START = 'dc_transition_start'
    DC_TRANSITION_END = 'dc_transition_end'
    DC_UI_MARKER = 'dc_ui_marker'
    DC_UI_PAUSE_ENTER = 'dc_ui_pause_enter'
    DC_UI_PAUSE_EXIT = 'dc_ui_pause_exit'
    DC_UI_EXIT = 'dc_ui_exit'
    DC_UI_MARKER_SHOW_ADDITIONAL_INFO = 'dc_ui_marker_add_info'
    DC_UI_MARKER_STATES: dict

class KillCamSoundPlayer(CallbackPauseManager, IViewComponentsCtrlListener):
    sessionProvider: Any
    __transitionDuration: Any
    def __init__(self):
        ...
    @property
    def __isSimplifiedDC(self):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def __onKillCamInterrupted(self):
        ...
    def __muteGameAudio(self, mute):
        ...
    def __playSoundNotification(self, notificationName=None, position=None):
        ...
    def __onKillCamModeEffectsPlaced(self, isSpotted):
        ...
    def __trajectoryProgress(self, configMovementDuration):
        ...
    def __onCamMovementStart(self, configMovementDuration):
        ...
    def __startTrajectoryProgress(self, configMovementDuration):
        ...
    def __stopTrajectoryProgress(self):
        ...
    def __onFollowTrajectoryEnd(self):
        ...
    def __playBlackFadeIn(self, leaveKillCam):
        ...
    def __resetRTPCTrajectoryProgress(self):
        ...
    def __playBlackFadeOut(self, leaveKillCam):
        ...
    def __onMarkerDisplayChanged(self, markerState, ctx):
        ...
    def __onKillCamStateChange(self, killCamState, _):
        ...
