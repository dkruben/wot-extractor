# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/map_zones/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from constants import MinimapLayerType as MinimapLayerType
from gui.Scaleform.daapi.view.battle.shared.map_zones.mixins import MapZonesListener as MapZonesListener
from gui.Scaleform.daapi.view.battle.shared.minimap import common as common, settings as settings
from gui.Scaleform.genConsts.BATTLE_MINIMAP_CONSTS import BATTLE_MINIMAP_CONSTS as BATTLE_MINIMAP_CONSTS
from helpers import unicodeToStr as unicodeToStr
_logger: Any
_layerTypesMapping: dict

class MapZonesEntriesPlugin(common.EntriesPlugin, MapZonesListener):
    MINIMAP_ENTRY_SYMBOL = 'ScenarioMinimapEntry'
    __mmLayers: Any
    def __init__(self, parent, clazz=None):
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
    def _onZoneTransformed(self, zone):
        ...
    def _onTransformedZoneRemoved(self, zone):
        ...
    def __addTransromedZone(self, zone):
        ...
    def __addMarkerToZone(self, zoneMarker, matrix):
        ...
    def __removeMarkerFromZone(self, zoneMarker):
        ...
    def __updateProgress(self, zoneMarker):
        ...
