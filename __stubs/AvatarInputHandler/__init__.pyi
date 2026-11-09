# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
import math as math
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import CGF as CGF
import Keys as Keys
import Math as Math
import ResMgr as ResMgr
import Input as Input
from AvatarInputHandler.AimingSystems import disableShotPointCache as disableShotPointCache
from AvatarInputHandler.commands.armor_flashlight_control import ArmorFlashlightControl as ArmorFlashlightControl
from AvatarInputHandler.commands.prebattle_highlights_control import PrebattleHighlightsCommandsSetup as PrebattleHighlightsCommandsSetup
from AvatarInputHandler.vehicles_selection_mode import VehiclesSelectionControlMode as VehiclesSelectionControlMode
from AvatarInputHandler.commands.fl_random_reserves import FLRandomReserves as FLRandomReserves
from aih_constants import MAP_CASE_MODES as MAP_CASE_MODES
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
import BattleReplay as BattleReplay
import CommandMapping as CommandMapping
import GenericComponents as GenericComponents
import TriggersManager as TriggersManager
import aih_constants as aih_constants
import constants as constants
from AvatarInputHandler import AimingSystems as AimingSystems, keys_handlers as keys_handlers, aih_global_binding as aih_global_binding, gun_marker_ctrl as gun_marker_ctrl, steel_hunter_control_modes as steel_hunter_control_modes, MapCaseMode as MapCaseMode, RespawnDeathMode as RespawnDeathMode, cameras as cameras, control_modes as control_modes, kill_cam_modes as kill_cam_modes
from BigWorld import SniperAimingSystem as SniperAimingSystem
from AvatarInputHandler.DynamicCameras import ArcadeCamera as ArcadeCamera, ArtyCamera as ArtyCamera, DualGunCamera as DualGunCamera, SniperCamera as SniperCamera, StrategicCamera as StrategicCamera, kill_cam_camera as kill_cam_camera, twin_gun_camera as twin_gun_camera
from AvatarInputHandler.commands.dualgun_control import DualGunController as DualGunController
from AvatarInputHandler.commands.mechanic_controls import createMechanicControls as createMechanicControls
from AvatarInputHandler.commands.prebattle_setups_control import PrebattleSetupsControl as PrebattleSetupsControl
from AvatarInputHandler.commands.radar_control import RadarControl as RadarControl
from AvatarInputHandler.commands.siege_mode_control import SiegeModeControl as SiegeModeControl
from AvatarInputHandler.commands.vehicle_upgrade_control import VehicleUpdateControl as VehicleUpdateControl
from AvatarInputHandler.commands.vehicle_upgrade_control import VehicleUpgradePanelControl as VehicleUpgradePanelControl
from AvatarInputHandler.commands.dev_commands_control import createDevCommandsControl as createDevCommandsControl
from AvatarInputHandler.remote_camera_sender import RemoteCameraSender as RemoteCameraSender
from Event import Event as Event
from Input import InputLayer as InputLayer
from TriggersManager import TRIGGER_TYPE as TRIGGER_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ARENA_PERIOD as ARENA_PERIOD, AIMING_MODE as AIMING_MODE
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui import g_guiResetters as g_guiResetters, GUI_CTRL_MODE_FLAG as GUI_CTRL_MODE_FLAG, GUI_SETTINGS as GUI_SETTINGS
from gui.app_loader import settings as settings
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from gui.shared.system_factory import collectPrebattleCtrlMode as collectPrebattleCtrlMode
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from AvatarInputHandler.player_notifications.siege_mode.notifier import SiegeModeNotifier as SiegeModeNotifier
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from components_base.component_descriptor import ComponentDescriptor as ComponentDescriptor
from components_base.component_controller import ComponentController as ComponentController
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from avatar_components.avatar_input_debug import AvatarInputDebug as AvatarInputDebug
from BigWorld import KeyEvent as KeyEvent, MouseEvent as MouseEvent, AxisEvent as AxisEvent
INPUT_HANDLER_CFG = 'gui/avatar_input_handler.xml'
_logger: Any
_CTRL_TYPE = aih_constants.CTRL_TYPE
_ARTY_CTRL_TYPE: Any
_ShakeReason = aih_constants.ShakeReason
_CTRL_MODE = aih_constants.CTRL_MODE_NAME
_GUN_MARKER_TYPE = aih_constants.GUN_MARKER_TYPE
_GUN_MARKER_FLAG = aih_constants.GUN_MARKER_FLAG
_BINDING_ID = aih_global_binding.BINDING_ID
_CTRL_MODES = aih_constants.CTRL_MODES
_CTRLS_FIRST = _CTRL_MODE.DEFAULT
_CONTROL_MODE_SWITCH_COOLDOWN = 1.0
_CTRLS_DESC_MAP: dict
DISABLE_CTRL_SWITCH_CAPS_MAP: dict
OVERWRITE_CTRLS_DESC_MAP: dict
_DYNAMIC_CAMERAS: tuple
_FREE_AND_CHAT_SHORTCUT_CMD: tuple

class DynamicCameraSettings(object):
    settings: Any
    __dynamic: Any
    def __init__(self, dataSec):
        ...
    def getGunImpulse(self, caliber):
        ...
    def getSensitivityToImpulse(self, vehicleMass):
        ...
    def __readRange(self, dataSec):
        ...

class AvatarInputHandler(CallbackDelayer, ComponentController):
    ctrl: Any
    ctrls: Any
    isSPG: Any
    isATSPG: Any
    isDualGun: Any
    isTwinGun: Any
    isMagneticAimEnabled: Any
    isFlashBangAllowed: Any
    isDetached: Any
    isGuiVisible: Any
    isStarted: Any
    isObserverFPV: Any
    remoteCameraSender: Any
    __ctrlModeName: Any
    __aimOffset: Any
    _DYNAMIC_CAMERAS_ENABLED_KEY = 'global/dynamicCameraEnabled'
    settingsCore: Any
    appLoader: Any
    siegeModeControl: Any
    dualGunControl: Any
    siegeModeNotifier: Any
    DEFAULT_AIH_WORLD_ID = -1
    __alwaysShowAimKey: Any
    __showMarkersKey: Any
    onCameraChanged: Any
    onPostmortemKillerVisionEnter: Any
    onPostmortemKillerVisionExit: Any
    onReceivedKillerID: Any
    OnVehicleCollided: Any
    __isArenaStarted: Any
    __isStarted: Any
    __targeting: Any
    __vertScreenshotCamera: Any
    __ctrls: Any
    __killerVehicleID: Any
    __deathReasonID: Any
    __isAutorotation: Any
    __prevModeAutorotation: Any
    __isSPG: Any
    __isATSPG: Any
    __isDualGun: Any
    __isTwinGun: Any
    __isMagnetAimEnabled: Any
    __curCtrl: Any
    __isDetached: Any
    __pendingModeSwitch: Any
    __observerVehicle: Any
    __commands: Any
    __detachedCommands: Any
    __persistentCommands: Any
    __remoteCameraSender: Any
    __isGUIVisible: Any
    __lastSwitchTime: Any
    __inputDebug: Any
    __dynamicCameraSettings: Any
    @staticmethod
    def enableDynamicCamera(enable, useHorizontalStabilizer=True):
        ...
    @staticmethod
    def enableHullLock(enable):
        ...
    @staticmethod
    def isCameraDynamic():
        ...
    @staticmethod
    def isSniperStabilized():
        ...
    @staticmethod
    def isHullLockEnabled():
        ...
    @property
    def ctrlModeName(self):
        ...
    def __init__(self):
        ...
    def __constructComponents(self):
        ...
    def prerequisites(self):
        ...
    def handleKeyEvent(self, event):
        ...
    def handleMouseEvent(self, event):
        ...
    def handleAxisEvent(self, event):
        ...
    def setForcedGuiControlMode(self, flags):
        ...
    def updateShootingStatus(self, canShoot):
        ...
    def getDesiredShotPoint(self, ignoreAimingMode=False):
        ...
    def getMarkerPoint(self):
        ...
    def showClientGunMarkers(self, isShown):
        ...
    def showServerGunMarker(self, isShown):
        ...
    def updateClientGunMarker(self, gunMarkerInfo, supportMarkersInfo, relaxTime):
        ...
    def updateServerGunMarker(self, gunMarkerInfo, supportMarkersInfo, relaxTime):
        ...
    def updateDualAccGunMarker(self, gunMarkerInfo, supportMarkersInfo, relaxTime):
        ...
    def setAimingMode(self, enable, mode):
        ...
    def getAimingMode(self, mode):
        ...
    def setAutorotation(self, bValue, triggeredByKey=False):
        ...
    def getAutorotation(self):
        ...
    def switchAutorotation(self, triggeredByKey=False):
        ...
    def activatePostmortem(self):
        ...
    def movingToRespawnBase(self):
        ...
    def deactivatePostmortem(self):
        ...
    def setKillerVehicleID(self, killerVehicleID, deathReasonID=None):
        ...
    def getKillerVehicleID(self):
        ...
    def getDeathReason(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def __onVehicleMatrixBindingChanged(self, isStatic):
        ...
    def setObservedVehicle(self, vehicleID):
        ...
    # decorador original: @disableShotPointCache
    def onControlModeChanged(self, eMode, **kwargs):
        ...
    def onObserverControlModeChanged(self, eMode):
        ...
    def getTargeting(self):
        ...
    def setGUIVisible(self, isVisible):
        ...
    def selectPlayer(self, vehId):
        ...
    def onMinimapClicked(self, worldPos):
        ...
    def onVehicleShaken(self, vehicle, shakeReason, impulsePosition, impulseDir, caliber, sensitivity=1.0):
        ...
    def onVehicleCollision(self, vehicle, impactVelocity):
        ...
    def onVehicleDeath(self, vehicle, exploded):
        ...
    def onExplosionImpulse(self, position, impulseValue):
        ...
    def onProjectileHit(self, position, caliber, sensitivity, isOwnShot):
        ...
    def onSpecificImpulse(self, position, impulse, specificCtrl=None):
        ...
    def notifyCameraChanged(self):
        ...
    def __adjustImpulse(self, impulseDir, impulseValue, camera, impulsePosition, vehicleSensitivity, impulseReason):
        ...
    def __identifyVehicleType(self):
        ...
    def reloadDynamicSettings(self):
        ...
    def _readCfg(self):
        ...
    def __setupCtrls(self, section):
        ...
    def __checkSections(self, section):
        ...
    def __onArenaStarted(self, period, *args):
        ...
    def __canReceiveServerGunMarker(self):
        ...
    def __onRecreateDevice(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def isControlModeChangeAllowed(self):
        ...
    @classmethod
    def isAllowToSwitchPositionOrFPV(cls):
        ...
    @classmethod
    def isToControlModeSwitchEnabled(cls, eMode):
        ...
    def __setInitialControlMode(self):
        ...
    def __isModeSwitchInPrebattlePossible(self, eMode):
        ...

class _Targeting(object):
    __mouseMatProv: Any
    def __init__(self):
        ...
    def isEnabled(self):
        ...
    def getTargetEntity(self):
        ...
    def enable(self, flag):
        ...
    def onRecreateDevice(self):
        ...
    def detach(self, value):
        ...

class _VertScreenshotCamera(object):
    isEnabled: Any
    __isEnabled: Any
    __savedCamera: Any
    __savedWatchers: Any
    __nearPlane: Any
    __farPlane: Any
    __watcherNames: Any
    __cam: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def enable(self, doEnable):
        ...

def addEmptyIfNotExits(name):
    ...
