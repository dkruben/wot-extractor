# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ClientSelectableCameraObject.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from ClientSelectableObject import ClientSelectableObject as ClientSelectableObject
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class ClientSelectableCameraObject(ClientSelectableObject):
    hangarSpace: Any
    allCameraObjects: Any
    __state: Any
    def __init__(self, name='ClientSelectableCameraObject'):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    @classmethod
    def switchCamera(cls, clickedObject=None, cameraName=None, instantly=False):
        ...
    @classmethod
    def deselectAll(cls):
        ...
    def onSelect(self, instantly=False):
        ...
    def onDeselect(self):
        ...
    def setState(self, state):
        ...
    @property
    def state(self):
        ...
