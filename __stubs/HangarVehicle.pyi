# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/HangarVehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraDistanceModes as CameraDistanceModes
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle as ClientSelectableCameraVehicle
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events

class HangarVehicle(ClientSelectableCameraVehicle):
    hangarSpace: Any
    selectionId: Any
    clickSoundName: Any
    releaseSoundName: Any
    mouseOverSoundName: Any
    edgeMode: Any
    modelName: Any
    camDistState: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    def __onSpaceCreated(self):
        ...
    def _setStartValues(self):
        ...
    def __changeVehicleModelTransform(self, event):
        ...
    def __resetVehicleModelTransform(self, event):
        ...
