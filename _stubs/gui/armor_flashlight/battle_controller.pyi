# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/armor_flashlight/battle_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
import armor_flashlight as armor_flashlight
from AvatarInputHandler import aih_global_binding as aih_global_binding, AvatarInputHandler as AvatarInputHandler
from AvatarInputHandler.aih_global_binding import BINDING_ID as BINDING_ID
from AvatarInputHandler.gun_marker_ctrl import computePiercingPowerAtDist as computePiercingPowerAtDist
from Math import Vector3 as Vector3
from Vehicle import Vehicle as Vehicle
from account_helpers.settings_core.settings_constants import ArmorFlashlight as ArmorFlashlight, GRAPHICS as GRAPHICS, POST_PROCESSING_QUALITY as POST_PROCESSING_QUALITY
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME, GUN_MARKER_FLAG as GUN_MARKER_FLAG, GUN_MARKER_TYPE as GUN_MARKER_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import SHELL_TYPES_INDICES as SHELL_TYPES_INDICES
from gui.armor_flashlight.config import getConfig as getConfig, isFeatureEnabled as isFeatureEnabled
from gui.armor_flashlight.interfaces import IArmorFlashlightBattleController as IArmorFlashlightBattleController
from gui.armor_flashlight.utils import getAllMatInfos as getAllMatInfos, ArmorFlashlightHideReason as ArmorFlashlightHideReason
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.shared.utils.functions import getShellImpactParams as getShellImpactParams
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from shared_utils import BitmaskHelper as BitmaskHelper
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from ProjectileMover import EntityCollisionData as EntityCollisionData
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from aih_constants import GunMarkerState as GunMarkerState
_logger: Any
GUN_PIERCING = 'gunPiercing'
SETTINGS_TRIGGER_CHANGES: tuple
VALID_CTRL_MODES: tuple

class ArmorFlashlightBattleController(IArenaLoadController, IArmorFlashlightBattleController):
    sessionProvider: Any
    settingsCore: Any
    gunMarkersFlags: Any
    clientMarkerDataProvider: Any
    serverMarkerDataProvider: Any
    zoomFactor: Any
    _myTeam: Any
    _cachedVehicleData: Any
    _targetTankID: Any
    _hideReasons: Any
    _armorFlashlightSingleton: Any
    def __init__(self):
        ...
    def stopControl(self):
        ...
    def spaceLoadCompleted(self):
        ...
    def getControllerID(self):
        ...
    def toggle(self):
        ...
    def addHideReason(self, reason):
        ...
    def removeHideReason(self, reason):
        ...
    def _subscribeToBattleSessionEvents(self, *_, **__):
        ...
    def _unsubscribeFromBattleSessionEvents(self, *_, **__):
        ...
    def _onCrosshairViewChanged(self, viewID):
        ...
    def _updateVisibilityState(self, markerType, gunMarkerState, *_, **__):
        ...
    def _hide(self):
        ...
    def _setShootingParams(self, hitPoint, direction, gunAimingCircleSize):
        ...
    def _stopFlashlight(self):
        ...
    def _startFlashlight(self, vehicle):
        ...
    def _resolveTargetTank(self, appearing):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def _setSettings(self):
        ...
    def _onArenaVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...
    def __updateArmorFlashlightSingletonVisibility(self):
        ...

def _inputIsBad(handler):
    ...
def _collisionIsBad(collision, myTeam):
    ...
