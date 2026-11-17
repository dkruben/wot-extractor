# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/avatar_input_handler/control_modes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import GUI as GUI
import Keys as Keys
import Math as Math
import SoundGroups as SoundGroups
import math_utils as math_utils
from AvatarInputHandler import aih_global_binding as aih_global_binding
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera as ArcadeCamera
from AvatarInputHandler.DynamicCameras.StrategicCamera import StrategicCamera as StrategicCamera
from AvatarInputHandler.MapCaseMode import AracdeMinefieldControleMode as AracdeMinefieldControleMode, MapCaseControlMode as MapCaseControlMode
from AvatarInputHandler.control_modes import IControlMode as IControlMode, ArcadeControlMode as ArcadeControlMode, SniperControlMode as SniperControlMode
from Vehicle import Vehicle as Vehicle
from account_helpers.settings_core import settings_constants as settings_constants
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import AIMING_MODE as AIMING_MODE
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode.gui.app_loader import observers as observers
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY, EQUIPMENT_STAGES as STAGES, VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
from ResMgr import DataSection as DataSection
from story_mode_common.items.sm_artefacts import BaseAbilityEquipment as BaseAbilityEquipment

class StoryModeArcadeCamera(ArcadeCamera):
    _START_DISTANCE = 10
    _START_ANGLE = 80
    def create(self, onChangeControlMode=None, postmortemMode=False, smartPointCalculator=True):
        ...

class StoryModeArcadeControlModeStartCamera(ArcadeControlMode):
    _cam: Any
    def _setupCamera(self, dataSection):
        ...

class LockTargetDisabler(IControlMode):
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def _isLockTargetDisabled(self):
        ...

class OnboardingArcadeControlMode(LockTargetDisabler, StoryModeArcadeControlModeStartCamera):
    _storyModeCtrl: Any
    @property
    def isWinMessageShown(self):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def onChangeControlModeByScroll(self):
        ...
    def _isLockTargetDisabled(self):
        ...

class OnboardingSniperControlMode(LockTargetDisabler, SniperControlMode):
    _storyModeCtrl: Any
    def _isLockTargetDisabled(self):
        ...

class StoryModeArcadeControlMode(LockTargetDisabler, StoryModeArcadeControlModeStartCamera):
    def _isLockTargetDisabled(self):
        ...

class StoryModeSniperControlMode(LockTargetDisabler, SniperControlMode):
    def _isLockTargetDisabled(self):
        ...

class StoryModeArcadeMinefieldControlMode(AracdeMinefieldControleMode):
    ...

class SMStrategicCamera(StrategicCamera):
    _TICK_TIME = 0.01
    minApplyRadius: Any
    maxApplyRadius: Any
    _lastPosition: Any
    _tickID: Any
    def __init__(self, dataSec):
        ...
    def update(self, dx, dy, dz, rotateMode=True, zoomMode=True, updatedByKeyboard=False):
        ...
    def enable(self, targetPos, saveDist, switchToPos=None, switchToPlace=None):
        ...
    def disable(self):
        ...
    @staticmethod
    def _getConfigsKey():
        ...
    @staticmethod
    def _getPlayerPosition():
        ...
    def _tick(self):
        ...

class SMStrategicMapCaseControlMode(MapCaseControlMode):
    MODE_NAME = CTRL_MODE_NAME.SM_STRATEGIC
    _acceptsArcadeState: Any
    def enable(self, **args):
        ...
    def _createCamera(self, config, offset=...):
        ...

class SMEntityViewMode(IControlMode):
    _guiSessionProvider: Any
    _aimOffset: Any
    _MOVE_CMDS: tuple
    _cam: Any
    _entityID: Any
    _isEnabled: Any
    def __init__(self, dataSection, _):
        ...
    @property
    def curVehicleID(self):
        ...
    @property
    def camera(self):
        ...
    def isSelfVehicle(self):
        ...
    def isEnabled(self):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def enable(self, **args):
        ...
    def disable(self):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def _showMessage(self, msgName, args):
        ...

def targetIsBunker():
    ...
