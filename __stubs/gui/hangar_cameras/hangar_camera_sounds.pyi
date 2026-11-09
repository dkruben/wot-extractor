# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from SoundGroups import g_instance as SoundGroupsInstance
from skeletons.gui.hangar_cameras import IHangarCameraSounds as IHangarCameraSounds
from gui.shared import g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents, CameraMovementStates as CameraMovementStates

class HangarCameraSounds(IHangarCameraSounds):
    hangarSpace: Any
    __isMainView: Any
    class _MoveCameraEvents(object):
        MOVE_TO_HERO = 'ue_hangar_generic_camera_fly_forward'
        MOVE_TO_MAIN = 'ue_hangar_generic_camera_fly_backward'
    class _CameraStates(object):
        STATE_NAME = 'STATE_hangar_camera_state_rotate_or_onproposal'
        MAIN_VEHICLE_AND_NOT_IN_IDLE = 'STATE_hangar_camera_state_rotate_or_onproposal_false'
        HERO_VEHICLE_OR_IN_IDLE = 'STATE_hangar_camera_state_rotate_or_onproposal_true'
    class _SelectedVehicleStates(object):
        STATE_NAME = 'STATE_hangar_tank_view'
        HERO_VEHICLE = 'STATE_hangar_tank_view_proposal'
        MAIN_VEHICLE = 'STATE_hangar_tank_view_main'
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def playMotionToObject(self):
        ...
    def playMotionToMain(self):
        ...
    def __handleEntityUpdated(self, event):
        ...
    def __playMotionSounds(self, isMainView, state=None):
        ...
    def __handleIdleCameraActivation(self, event):
        ...
