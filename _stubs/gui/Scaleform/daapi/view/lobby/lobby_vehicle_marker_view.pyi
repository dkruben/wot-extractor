# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/lobby_vehicle_marker_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from collections import defaultdict as defaultdict
import GUI as GUI
import Math as Math
from gui.Scaleform.daapi.view.meta.LobbyVehicleMarkerViewMeta import LobbyVehicleMarkerViewMeta as LobbyVehicleMarkerViewMeta
from gui.shared.gui_items.Vehicle import getVehicleClassTag as getVehicleClassTag
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents, CameraMovementStates as CameraMovementStates
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from frameworks.wulf.gui_constants import WindowLayer as WindowLayer
from frameworks.wulf import WindowStatus as WindowStatus
from cgf_components.marker_component import LobbyFlashMarker as LobbyFlashMarker

class LobbyVehicleMarkerView(LobbyVehicleMarkerViewMeta):
    __LAYERS_WITHOUT_MARKERS: set
    hangarSpace: Any
    guiLoader: Any
    __markersCache: Any
    __isMarkerDisabled: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onSpaceDestroy(self, _):
        ...
    def __onHeroTankLoaded(self, event):
        ...
    def _onPlatoonTankLoaded(self, event):
        ...
    def _onHeroPlatoonTankDestroy(self, event):
        ...
    def addCgfMarker(self, entityId, markerComponent, matrix):
        ...
    def removeCgfMarker(self, entityId):
        ...
    def __onCameraEntityUpdated(self, event):
        ...
    def __updateMarkerVisibility(self, vehicleId):
        ...
    def __updateAllMarkersVisibility(self):
        ...
    def _canShowMarkers(self):
        ...
    @staticmethod
    def __getVehicleInfo(vehicle):
        ...
    @staticmethod
    def __getCorrectedHPGuiMatrix(vehicle):
        ...
    def __beginCreateVehicleMarker(self, vehicle):
        ...
    def __createVehicleMarker(self, vehicle):
        ...
    def __createPlatoonMarker(self, vehicle, playerName):
        ...
    def __destroyMarker(self, entityId):
        ...
    def __destroyAllMarkers(self):
        ...
    def __onWindowStatusChanged(self, uniqueID, newStatus):
        ...
