# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicle_to_camera_alignment_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
import DebugDrawer as DebugDrawer
import Math as Math
import math_utils as math_utils
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from CameraComponents import CameraComponent as CameraComponent
from constants import IS_CLIENT as IS_CLIENT
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from cgf_script.registration import registerComponent as registerComponent
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
from AvatarInputHandler.cameras import getViewProjectionMatrix as getViewProjectionMatrix
_logger: Any
_DEFAULT_SCREEN_TL_CORNER: Any
_DEFAULT_SCREEN_BR_CORNER: Any
g_alignmentCameraVisuals: Any

class _AlignmentCameraVisuals(object):
    enabled: Any
    def __init__(self):
        ...
    def toggle(self):
        ...
    def draw(self, aabbCenter, vehicleSize, frameCenter):
        ...

# decorador original: @registerComponent
class VehicleToCameraAlignmentComponent(object):
    category = 'Vehicle'
    editorTitle = 'Vehicle To Camera Alignment Component'
    serialName = 'BW::VehicleToCameraAlignmentComponent'
    domain = CGF.Domain.ClientEditor

class VehicleToCameraAlignmentSystem(CGF.System):
    _hangarSpace: Any
    Veh2CamAlignmentActivate: Any
    Veh2CamAlignmentIterate: Any
    Reactions: Any
    __aabbCenter: Any
    __vehicleSize: Any
    __shouldAlignCenters: Any
    __screenWidth: Any
    __screenHeight: Any
    __resizeHandled: Any
    __screenTopLeftCorner: Any
    __screenBottomRightCorner: Any
    __callbackDelayer: Any
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    def alignCamera(self, cameraName):
        ...
    def getTargetPosition(self):
        ...
    def tick(self):
        ...
    def __onCameraSwitched(self, cameraName):
        ...
    def __handleResize(self, event):
        ...
    def __waitAABBLoaded(self):
        ...
    def __getHangarVehicleCenter(self):
        ...
    def __projectViewportToWorld(self, viewportPoint, depth):
        ...
    def __alignCenters(self):
        ...
