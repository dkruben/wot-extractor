# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.shared.events import HasCtxEvent as HasCtxEvent

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
