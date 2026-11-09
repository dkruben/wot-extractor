# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cameras/hangar_camera_common.py
from enum import Enum
from gui.shared.events import HasCtxEvent

class CameraMovementStates(object):
    ON_OBJECT = 0
    MOVING_TO_OBJECT = 1
    FROM_OBJECT = 2


class CameraDistanceModes(Enum):
    DEFAULT = 0
    CUSTOM = 1


class CameraRelatedEvents(HasCtxEvent):
    CAMERA_ENTITY_UPDATED = 'CameraEntityUpdate'
    IDLE_CAMERA = 'IdleCamera'
    VEHICLE_LOADING = 'VehicleLoading'
    LOBBY_VIEW_MOUSE_MOVE = 'MouseMove'
    FORCE_DISABLE_IDLE_PARALAX_MOVEMENT = 'cameraRelatedEvents/forceDisableIdleParalaxMovement'
    FORCE_DISABLE_CAMERA_MOVEMENT = 'cameraRelatedEvents/forceDisableCameraMovement'
    ON_RESIZE = 'OnResize'
