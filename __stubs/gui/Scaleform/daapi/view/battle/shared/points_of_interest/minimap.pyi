# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import math_utils as math_utils
from gui.Scaleform.daapi.view.battle.shared.minimap.common import EntriesPlugin as EntriesPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.settings import CONTAINER_NAME as CONTAINER_NAME
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.constants import POI_TYPE_UI_MAPPING as POI_TYPE_UI_MAPPING, POI_STATUS_UI_MAPPING as POI_STATUS_UI_MAPPING
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.poi_helpers import getPoiCooldownProgress as getPoiCooldownProgress
from points_of_interest.components import PoiStateUpdateMask as PoiStateUpdateMask
from points_of_interest.mixins import PointsOfInterestListener as PointsOfInterestListener
from points_of_interest_shared import PoiStatus as PoiStatus
from points_of_interest.components import PoiStateComponent as PoiStateComponent
_logger: Any
_POI_MINIMAP_ENTRY_SYMBOL = 'PoiMinimapEntry'

class PointsOfInterestPlugin(EntriesPlugin, PointsOfInterestListener):
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
    def __updateType(self, entryID, state):
        ...
    def __updateStatus(self, entryID, poiState):
        ...
    def __updateProgress(self, entryID, poiState):
        ...
    def __updateTeam(self, entryID, poiState):
        ...
    def __updateCooldownProgress(self, entryID, poiState):
        ...
    def __onBattleSessionStop(self):
        ...
