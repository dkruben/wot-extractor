# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/markers2d.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Math as Math
from gui.Scaleform.daapi.view.battle.shared.markers2d import plugins as plugins
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.constants import POI_TYPE_UI_MAPPING as POI_TYPE_UI_MAPPING, POI_STATUS_UI_MAPPING as POI_STATUS_UI_MAPPING
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.poi_helpers import getPoiCooldownProgress as getPoiCooldownProgress
from points_of_interest.components import PoiStateComponent as PoiStateComponent, PoiStateUpdateMask as PoiStateUpdateMask
from points_of_interest.mixins import PointsOfInterestListener as PointsOfInterestListener
from points_of_interest_shared import PoiStatus as PoiStatus
from helpers.fixed_dict import StatusWithTimeInterval as StatusWithTimeInterval
_logger: Any
_POI_MARKER_SYMBOL = 'PointOfInterestMarkerUI'
_POI_MARKER_POSITION_OFFSET: Any
_POI_MARKER_MIN_SCALE = 53
_POI_MARKER_BOUNDS: Any
_POI_MARKER_INNER_BOUNDS: Any
_POI_MARKER_CULL_DISTANCE = 1800
_POI_MARKER_BOUNDS_MIN_SCALE: Any

class PointsOfInterestPlugin(plugins.MarkerPlugin, PointsOfInterestListener):
    __markers: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def onPoiAdded(self, poiState):
        ...
    def onPoiRemoved(self, poiState):
        ...
    def onProcessPoi(self, poiState):
        ...
    def onPoiEntered(self, poiID):
        ...
    def onPoiLeft(self, poiID):
        ...
    def __initMarkers(self):
        ...
    def __destroyMarkers(self):
        ...
    def __updateType(self, markerID, state):
        ...
    def __updateStatus(self, markerID, poiState):
        ...
    def __updateProgress(self, markerID, poiState):
        ...
    def __updateTeam(self, markerID, poiState):
        ...
    def __updateCooldownProgress(self, markerID, poiState):
        ...
    def __setPoiMarkerVisibility(self, poiID, isVisible):
        ...
    def __isMarkerActive(self, poiID):
        ...
    def __onBattleSessionStop(self):
        ...
