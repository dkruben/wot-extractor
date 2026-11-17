# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/map_zones/markers2d.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
import Math as Math
import typing as typing
from gui.Scaleform.daapi.view.battle.shared.map_zones.mixins import MapZonesListener as MapZonesListener
from gui.Scaleform.daapi.view.battle.shared.markers2d import plugins as plugins
_logger: Any
_MS_MARKER_MIN_SCALE = 60.0
_MS_MARKER_BOUNDS: Any
_MS_MARKER_INNER_BOUNDS: Any
_MS_MARKER_CULL_DISTANCE = 1800
_MS_MARKER_BOUNDS_MIN_SCALE: Any

class MapZonesPlugin(plugins.MarkerPlugin, MapZonesListener):
    MINIMAP_ENTRY_SYMBOL = 'ScenarioMarkerUI'
    __markers: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _onMarkerToZoneAdded(self, zoneMarker, matrix):
        ...
    def _onMarkerFromZoneRemoved(self, zoneMarker):
        ...
    def _onMarkerProgressUpdated(self, zoneMarker):
        ...
    def __addMarkerToZone(self, zoneMarker, matrix):
        ...
    def __removeMarkerFromZone(self, zoneMarker):
        ...
    def __updateProgress(self, zoneMarker):
        ...
    def __destroyMarkers(self):
        ...
