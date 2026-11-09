# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/Sector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
import MapActivities as MapActivities
from constants import SECTOR_STATE as SECTOR_STATE
from debug_utils import LOG_DEBUG as LOG_DEBUG
import Math as Math
import items as items
from ReplayEvents import g_replayEvents as g_replayEvents
SECTOR_LOCATION_TO_MAP_ACTIVITY: dict
ID_IN_PLAYER_GROUP_TO_MAP_ACTIVITY_LEAD_TIME: dict
BORDER_VISUALISATION_DASH_DIMENSIONS: tuple
BORDER_VISUALISATION_GAP_LENGTH = 5

class Sector(BigWorld.Entity):
    __startDestructionCallback: Any
    model: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def set_lengthX(self, oldValue):
        ...
    def set_lengthZ(self, oldValue):
        ...
    def set_state(self, oldValue):
        ...
    def startSectorBombingMapActivities(self, actualTargetTime):
        ...
    def showBomb(self, position):
        ...
    def setSectorBombing(self, position, dir_, effectsIndex):
        ...
    def __explosionFinished(self):
        ...
    def __cancelCallback(self):
        ...
