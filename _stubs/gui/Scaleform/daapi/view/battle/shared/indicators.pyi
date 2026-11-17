# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/indicators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from past.builtins import xrange as xrange
import BigWorld as BigWorld
import GUI as GUI
import SCALEFORM as SCALEFORM
import SoundGroups as SoundGroups
from account_helpers.settings_core.settings_constants import SOUND as SOUND, DAMAGE_INDICATOR as DAMAGE_INDICATOR, GRAPHICS as GRAPHICS
from constants import VEHICLE_SIEGE_STATE as _SIEGE_STATE, DIRECT_DETECTION_TYPE as DIRECT_DETECTION_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_WARNING as LOG_WARNING
from gui import DEPTH_OF_Aim as DEPTH_OF_Aim, GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.view.battle.shared.legacy_mechanics import siege_component as siege_component
from gui.Scaleform.daapi.view.meta.SiegeModeIndicatorMeta import SiegeModeIndicatorMeta as SiegeModeIndicatorMeta
from gui.Scaleform.daapi.view.meta.SixthSenseMeta import SixthSenseMeta as SixthSenseMeta
from gui.Scaleform.flash_wrapper import Flash as Flash, InputKeyMode as InputKeyMode
from gui.Scaleform.genConsts.DAMAGEINDICATOR import DAMAGEINDICATOR as DAMAGEINDICATOR
from gui.Scaleform.genConsts.SIEGE_MODE_CONSTS import SIEGE_MODE_CONSTS as SIEGE_MODE_CONSTS
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from gui.battle_control.battle_constants import DEVICE_STATES_RANGE as DEVICE_STATES_RANGE, DEVICE_STATE_NORMAL as DEVICE_STATE_NORMAL, DEVICE_STATE_CRITICAL as DEVICE_STATE_CRITICAL, VEHICLE_DEVICE_IN_COMPLEX_ITEM as VEHICLE_DEVICE_IN_COMPLEX_ITEM, DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN as HIT_INDICATOR_MAX_ON_SCREEN
from gui.battle_control.battle_constants import PREDICTION_INDICATOR_MAX_ON_SCREEN as PREDICTION_INDICATOR_MAX_ON_SCREEN
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.battle_control.controllers.hit_direction_ctrl import IHitIndicator as IHitIndicator, HitType as HitType
from gui.battle_control.controllers.spotting_indicators_ctrl import ISpottingIndicator as ISpottingIndicator, bindSpottingIndicator as bindSpottingIndicator, unbindSpottingIndicator as unbindSpottingIndicator
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.crits_mask_parser import critsParserGenerator as critsParserGenerator
from helpers import dependency as dependency
from helpers import i18n as i18n
from helpers.time_utils import MS_IN_SECOND as MS_IN_SECOND
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from soft_exception import SoftException as SoftException
from gui.battle_control import avatar_getter as avatar_getter
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from items.vehicles import VehicleDescriptor as VehicleDescriptor
_DIRECT_INDICATOR_SWF = 'battleDirectionIndicatorApp.swf'
_DIRECT_INDICATOR_COMPONENT = 'WGDirectionIndicatorFlash'
_DIRECT_INDICATOR_MC_NAME = '_root.directionalIndicatorMc'
_DIRECT_ARTY_INDICATOR_MC_NAME = '_root.artyDirectionalIndicatorMc'
_DIRECT_INDICATOR_SWF_SIZE: tuple
_MARKER_SMALL_SIZE_THRESHOLD = 0.1
_MARKER_LARGE_SIZE_THRESHOLD = 0.3
_VIEWS_WITH_INV_CAMERA_ORIENTATION: tuple
_EXTENDED_MARKER_TYPE_TO_CIRCLE_BG: dict
_EXTENDED_BLIND_MARKER_TYPE_TO_CIRCLE_BG: dict
_CRITICAL_DAMAGE_TYPE_TO_CIRCLE_BG: dict
_STANDARD_MARKER_TYPE_TO_BG: dict
_STANDARD_BLIND_MARKER_TYPE_TO_BG: dict
_EXTENDED_MARKER_TYPE_TO_BG: dict
_EXTENDED_BLIND_MARKER_TYPE_TO_BG: dict
_MARKER_TYPE_TO_PRIORITY: dict

class _MARKER_TYPE(CONST_CONTAINER):
    HP_DAMAGE = 0
    HP_ALLAY_DAMAGE = 1
    BLOCKED_DAMAGE = 2
    CRITICAL_DAMAGE = 3

class _MARKER_SIZE_TYPE(CONST_CONTAINER):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

class DAMAGE_INDICATOR_TYPE(CONST_CONTAINER):
    STANDARD = 0
    EXTENDED = 1

class _MarkerData(object):
    idx: Any
    timeLeft: Any
    hitData: Any
    markerType: Any
    isBlind: Any
    def __init__(self, idx, timeLeft, hitData, isBlind=False):
        ...
    @staticmethod
    def __getMarkerType(hitData):
        ...

class _MarkerVOBuilder(object):
    def buildVO(self, markerData):
        ...
    def _getIndicatorFrameRate(self):
        ...
    def _getBackground(self, markerData):
        ...

class _StandardMarkerVOBuilder(_MarkerVOBuilder):
    def _getBackground(self, markerData):
        ...

class _ExtendedMarkerVOBuilder(_MarkerVOBuilder):
    __dynamicIndicatorSize: Any
    def __init__(self, dynamicIndicatorSize):
        ...
    def buildVO(self, markerData):
        ...
    def _getBackground(self, markerData):
        ...
    def _getCircleBackground(self, markerData):
        ...
    def _getTankType(self, markerData):
        ...
    def _getDamageLabel(self, markerData):
        ...
    def _getSizeType(self, hp, damage):
        ...

class _ExtendedCriticalMarkerVOBuilder(_ExtendedMarkerVOBuilder):
    def _getCircleBackground(self, markerData):
        ...
    def _getDamageLabel(self, markerData):
        ...
    @staticmethod
    def _getCritType(mask):
        ...
    @staticmethod
    def _makeCritType(mask, isAlly):
        ...

class _AbstractMarkerVOBuilderFactory(object):
    def getVOBuilder(self, markerData):
        ...
    def buildMarkerVO(self, markerData):
        ...

class _ExtendedMarkerVOBuilderFactory(_AbstractMarkerVOBuilderFactory):
    __isIndicatorSizeDynamic: Any
    def __init__(self, isIndicatorSizeDynamic):
        ...
    def getVOBuilder(self, markerData):
        ...

class _StandardMarkerVOBuilderFactory(_AbstractMarkerVOBuilderFactory):
    def getVOBuilder(self, markerData):
        ...

class DamageIndicatorMeta(Flash):
    _as_updateSettings: Any
    _as_showStandard: Any
    _as_showExtended: Any
    _as_setYaw: Any
    _as_hide: Any
    _as_setScreenSettings: Any
    _as_setPosition: Any
    def __init__(self, swf, className, args):
        ...
    def destroy(self):
        ...
    def as_updateSettingsS(self, isStandard, isWithTankInfo, isWithAnimation, isWithValue):
        ...
    def as_showStandardS(self, itemIdx, bgStr, frame, priority):
        ...
    def as_showExtendedS(self, itemIdx, bgStr, circleStr, frame, tankName, tankTypeStr, damageValue, isFriendlyFire, priority):
        ...
    def as_hideS(self, itemIdx):
        ...
    def as_setYawS(self, itemIdx, yaw):
        ...
    def as_setScreenSettingsS(self, scale, screenWidth, screenHeight):
        ...
    def as_setPosition(self, posX, posY):
        ...

class _DamageIndicator(DamageIndicatorMeta, IHitIndicator):
    _DEFAULT_DAMAGE_INDICATOR_TYPE = DAMAGE_INDICATOR_TYPE.EXTENDED
    _DAMAGE_INDICATOR_SWF = 'battleDamageIndicatorApp.swf'
    _DAMAGE_INDICATOR_COMPONENT = 'WGHitIndicatorFlash'
    _DAMAGE_INDICATOR_MC_NAME = '_root.dmgIndicator.hit_{0}'
    _DAMAGE_INDICATOR_SWF_SIZE: tuple
    _DAMAGE_INDICATOR_TOTAL_FRAMES = 160
    _BEGIN_ANIMATION_FRAMES = 11
    _DAMAGE_INDICATOR_FRAME_RATE = 24
    _BEGIN_ANIMATION_DURATION: Any
    _DAMAGE_INDICATOR_ANIMATION_DURATION: Any
    sessionProvider: Any
    settingsCore: Any
    __voBuilderFactory: Any
    __updateMethod: Any
    __isBlind: Any
    def __init__(self, hitsCount):
        ...
    def __del__(self):
        ...
    def getHitType(self):
        ...
    def destroy(self):
        ...
    def getDuration(self):
        ...
    def getBeginAnimationDuration(self):
        ...
    def invalidateSettings(self, diff=None):
        ...
    def showHitDirection(self, idx, hitData, timeLeft):
        ...
    def hideHitDirection(self, idx):
        ...
    def _getIndicatorType(self):
        ...
    def __onCrosshairPositionChanged(self, posX, posY):
        ...
    def __setUpVOBuilderFactoryAndUpdateMethod(self, indicatorType):
        ...
    def __setMarkersScale(self, scale=None):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...

class SixthSenseIndicator(SixthSenseMeta, ISpottingIndicator):
    sessionProvider: Any
    _sound: Any
    __isBound: Any
    def __init__(self):
        ...
    def getIndicatorTogglesByType(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _sixthSenseToggle(self, isVisible, force):
        ...
    def _isSixthSenseEnabled(self):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __updateBinding(self):
        ...
    def __setBound(self, shouldBind):
        ...

class SixthSenseSound(object):
    __settingsCore: Any
    __sessionProvider: Any
    __eventName: Any
    __sound: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def play(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __updateSoundEvent(self):
        ...

class TargetDesignatorUnspottedIndicator(SixthSenseMeta, ISpottingIndicator):
    def getIndicatorTogglesByType(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __toggle(self, isVisible, force):
        ...
    def __isEnabled(self):
        ...

class SightPointerUnderScanningIndicator(SixthSenseMeta, ISpottingIndicator):
    __SFX_WARNING_STATE = 'STATE_ext_abl_sp_wn'
    __SFX_WARNING_ON = 'gui_abl_sp_warning'
    __SFX_WARNING_STATE_ON = 'STATE_ext_abl_sp_wn_on'
    __SFX_WARNING_OFF = 'gui_abl_sp_warning_off'
    __SFX_WARNING_STATE_OFF = 'STATE_ext_abl_sp_wn_off'
    def getIndicatorTogglesByType(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __toggle(self, isVisible, force):
        ...
    def __isEnabled(self):
        ...

class SightPointerSpottedIndicator(SixthSenseMeta, ISpottingIndicator):
    __SOUND_SPOTTED = 'gui_abl_sp_spot'
    def getIndicatorTogglesByType(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __toggle(self, isVisible, force):
        ...
    def __isEnabled(self):
        ...

class SiegeModeIndicator(SiegeModeIndicatorMeta):
    sessionProvider: Any
    settingsCore: Any
    __isEnabled: Any
    __isAllowedByContext: Any
    __isRadialMenuOpened: Any
    _siegeState: Any
    _siegeDevice: Any
    _devices: Any
    _switchTime: Any
    _startTime: Any
    _switchTimeTable: Any
    _siegeComponent: Any
    _deviceStateConverter: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __hasSiegeMode(self, vTypeDesc):
        ...
    def __updateIndicatorView(self, isSmooth=False):
        ...
    def __updateDevicesView(self):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onCrosshairPositionChanged(self, *args):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __updateSiegeState(self, siegeState, switchTime):
        ...
    def __updateDevicesState(self, deviceName, _, realState):
        ...
    def __updateDestroyed(self, _):
        ...
    def __resetDevices(self):
        ...
    def __onBattleStarted(self):
        ...
    def __updateContextAvailability(self):
        ...
    def __onRadialMenuOpenChanged(self):
        ...
    def __updateRadialMenuOpened(self):
        ...
    def __updateVisibility(self):
        ...
    @classmethod
    def __getDeviceStateConverter(cls, vTypeDesc):
        ...
    @staticmethod
    def __hydraulicDeviceStateConverter(deviceName, state):
        ...
    @staticmethod
    def __trackWithinTrackDeviceStateConverter(deviceName, state):
        ...
    @staticmethod
    def __twinGunVehicleDeviceStateConverter(deviceName, state):
        ...
    @staticmethod
    def __turboshaftDeviceStateConverter(deviceName, state):
        ...
    @staticmethod
    def __getUIType(vTypeDesc):
        ...
    @staticmethod
    def __createDevicesMap(vTypeDesc):
        ...
    @staticmethod
    def __getDeviceStateLevel(device):
        ...

class IDirectionIndicator(object):
    def track(self, position):
        ...
    def setShape(self, shape):
        ...
    def setDistance(self, distance):
        ...
    def setPosition(self, position):
        ...
    def remove(self):
        ...

class _DirectionIndicator(Flash, IDirectionIndicator):
    flashSize: Any
    __isVisible: Any
    _dObject: Any
    def __init__(self, swf, mcName):
        ...
    def __del__(self):
        ...
    def setShape(self, shape):
        ...
    def setDistance(self, distance):
        ...
    def setPosition(self, position):
        ...
    def track(self, position):
        ...
    def remove(self):
        ...
    def setVisibility(self, isVisible):
        ...

class _DirectionIndicatorMessage(_DirectionIndicator):
    def setMessage(self, message):
        ...

class _ArtyDirectionIndicator(Flash, IDirectionIndicator):
    flashSize: Any
    __isVisible: Any
    _dObject: Any
    def __init__(self, swf):
        ...
    def __del__(self):
        ...
    def setShape(self, shape):
        ...
    def setPosition(self, position):
        ...
    def track(self, position):
        ...
    def remove(self):
        ...
    def setVisibility(self, isVisible):
        ...

class PredictionIndicatorMeta(Flash):
    _as_show: Any
    _as_setYaw: Any
    _as_hide: Any
    _as_setPosition: Any
    _as_setScreenSettings: Any
    def __init__(self, swf, className, args):
        ...
    def destroy(self):
        ...
    def as_showS(self, itemIdx):
        ...
    def as_hideS(self, itemIdx):
        ...
    def as_setYawS(self, itemIdx, yaw):
        ...
    def as_setPosition(self, posX, posY):
        ...
    def as_setScreenSettingsS(self, scale, screenWidth, screenHeight):
        ...

class _PredictionIndicator(PredictionIndicatorMeta, IHitIndicator):
    _PREDICTION_INDICATOR_SWF = 'battlePredictionIndicatorApp.swf'
    _PREDICTION_INDICATOR_COMPONENT = 'WGPredictionIndicatorFlash'
    _PREDICTION_INDICATOR_MC_NAME = '_root.predictionIndicator.hit_{0}'
    _PREDICTION_INDICATOR_SWF_SIZE: tuple
    _PREDICTION_INDICATOR_MAX_DUR = 20
    sessionProvider: Any
    settingsCore: Any
    def __init__(self, hitsCount):
        ...
    def __del__(self):
        ...
    def getHitType(self):
        ...
    def destroy(self):
        ...
    def getDuration(self):
        ...
    def getBeginAnimationDuration(self):
        ...
    def showHitDirection(self, idx, hitData, timeLeft):
        ...
    def hideHitDirection(self, idx):
        ...
    def __onCrosshairPositionChanged(self, posX, posY):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __setMarkersScale(self, scale=None):
        ...

def createDirectIndicator(swf=..., mcName=...):
    ...
def createDamageIndicator():
    ...
def createPredictionIndicator():
    ...
