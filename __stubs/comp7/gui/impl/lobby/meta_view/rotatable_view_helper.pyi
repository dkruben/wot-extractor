# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/rotatable_view_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from enum import Enum as Enum
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class Comp7Cameras(Enum):
    DEFAULT = 'Tank'
    SHOP = 'Comp7ShopCamera'
    PURCHASE = 'PreShopCameraStart'
    PRE_FLYBY = 'PreStartShopCamera'

class RotatableViewHelper(object):
    __hangarSpace: Any
    def getCameraManager(self):
        ...
    def getCameraEvents(self, viewModel):
        ...
    def switchCamera(self, cameraName, instantly):
        ...
    def resetCamera(self, duration=0):
        ...
    @staticmethod
    def __onMoveSpace(args=None):
        ...
    @staticmethod
    def __onMouseOver3dScene(args):
        ...
