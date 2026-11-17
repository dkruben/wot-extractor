# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/c11n_hangar_camera_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import math as math
import math_utils as math_utils
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.graphics import isLowPreset as isLowPreset
from items.components.c11n_constants import EASING_TRANSITION_DURATION as EASING_TRANSITION_DURATION
from helpers import dependency as dependency
from helpers.CallbackDelayer import TimeDeltaMeter as TimeDeltaMeter
from math_utils import extendBoundingBox as extendBoundingBox, getCenterFromBox as getCenterFromBox
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes, TankPartNames as TankPartNames
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem, DOFParams as DOFParams
_VERTICAL_OFFSET: tuple
_VERTICAL_EPSILON = 0.1
_WORLD_UP: Any
_CLOSE_DIST_CONSTRAINTS: Any
_STYLE_INFO_YAW: Any
_STYLE_INFO_PITCH: Any
_STYLE_INFO_MAX_CAMERA_DIST = 15
_STYLE_INFO_MAX_VEHICLE_WIDTH = 0.45
_STYLE_INFO_MAX_VEHICLE_HEIGHT = 0.3
_STYLE_INFO_VEHICLE_SCREEN_X_SHIFT: Any
_PROJECTION_DECALS_DIR_CLIP_COS = 0.8
_ATTACHMENT_MAX_PITCH: Any
CUSTOMIZATION_CAMERA_NAME = 'Customization'

class C11nCameraModes(object):
    START_STATE = 0
    PREVIEW = 1
    EMBLEM = 2
    ANCHOR = 3
    STYLE_INFO = 4

class C11nHangarCameraManager(TimeDeltaMeter):
    _settingsCore: Any
    _service: Any
    _hangarSpace: Any
    _prevCameraPosition: Any
    __currentMode: Any
    __c11nCamera: Any
    __screenSpaceOffset: Any
    __ctx: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @property
    def vEntity(self):
        ...
    @property
    def currentMode(self):
        ...
    def resetCustomizationCamera(self, resetRotation=True, resetDistance=True):
        ...
    def locateCameraOnDecal(self, location, width, slotId, relativeSize=0.5, forceRotate=False):
        ...
    def locateCameraOnAnchor(self, position, normal, up, slotId, forceRotate=False, customConstraints=False):
        ...
    def locateCameraToStyleInfoPreview(self):
        ...
    def enableMovementByMouse(self, enableRotation=True, enableZoom=True):
        ...
    def isStyleInfo(self):
        ...
    def __rotateTurretAndGun(self, slotId=None):
        ...
    def __getStyleInfoDOFParams(self, cameraPos):
        ...
    def __getCameraYawPitch(self, up, normal, clipCos=None, maxPitch=None):
        ...
