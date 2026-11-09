# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/points_of_interest/managers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
import CGF as CGF
import SoundGroups as SoundGroups
from points_of_interest.components import PoiStateComponent as PoiStateComponent, PoiVehicleStateComponent as PoiVehicleStateComponent, PoiStateUIListenerComponent as PoiStateUIListenerComponent, PoiCaptureBlockerStateComponent as PoiCaptureBlockerStateComponent, PoiStateUpdateMask as PoiStateUpdateMask
from points_of_interest.poi_view_states import PointViewStateUpdater as PointViewStateUpdater, VehicleViewStateUpdater as VehicleViewStateUpdater
from points_of_interest_shared import PoiStatus as PoiStatus

class PoiStateCreateSystem(CGF.System):
    StateActivated: Any
    StateDeactivated: Any
    StateIterate: Any
    VehicleStateActivated: Any
    VehicleStateDeactivated: Any
    VehicleStateIterate: Any
    ListenersIterate: Any
    Reactions: Any
    def update(self):
        ...

class PoiStateUpdateSystem(CGF.System):
    StateIterate: Any
    ListenersIterate: Any
    StateAccess: Any
    Reactions: Any
    def periodUpdate(self):
        ...
    def getStateAccess(self):
        ...
    def getStates(self):
        ...

class PoiViewStateSystem(CGF.System):
    PointStateActivated: Any
    PointStateIterate: Any
    PointStateDeactivated: Any
    PointStateAccess: Any
    BlockerVehicleStatesActivated: Any
    BlockerVehicleStatesDeactivated: Any
    BlockerVehicleStatesIterate: Any
    BlockerVehicleStatesAccess: Any
    Reactions: Any
    __pointViewState: Any
    __vehicleViewState: Any
    def __init__(self):
        ...
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def __pointViewStateUpdate(self, pointState, captureBlockerStateID):
        ...

class PoiSoundSystem(CGF.System):
    __POI_STOP_CAPTURE_BY_ENEMY = 'comp_7_siren_off'
    __POI_CAPTURED_BY_ALLY = 'comp_7_point_activated'
    __POI_CAPTURED_BY_ENEMY = 'comp_7_point_lost'
    __POI_START_CAPTURE_BY_ENEMY = 'comp_7_siren_on'
    __POI_AVAILABLE = 'comp_7_point_drone_on'
    __POI_NOT_AVAILABLE = 'comp_7_point_drone_off'
    StateActivated: Any
    StateDeactivated: Any
    StateIterate: Any
    TransformAccess: Any
    Reactions: Any
    __poiStates: Any
    __soundObjects: Any
    def __init__(self):
        ...
    def onMappingUnloaded(self):
        ...
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    @staticmethod
    def __isAllyCapture(invader):
        ...
    @staticmethod
    def __play2d(soundName):
        ...
    def __update(self, poiState, go):
        ...
    def __getSoundObjName(self, soundName, poiID):
        ...
    def __play3D(self, soundName, poiID, go):
        ...
    def __stop3D(self, soundObjName):
        ...
    def __get3d(self, soundName, soundObjName, go):
        ...
