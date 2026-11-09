# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/OfflineMapCreator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Math as Math
from ArenaType import g_cache as g_cache
import constants as constants
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from helpers import dependency as dependency
from skeletons.map_activities import IMapActivities as IMapActivities
_CFG: dict
_SPACE_NAME = None
_V_START_ANGLES = None
_V_START_POS = None
_CAM_START_DIST = None
_CAM_START_ANGLES = None
_CAM_START_TARGET_POS = None
_CAM_DIST_CONSTR = None
_CAM_PITCH_CONSTR = None
_CAM_YAW_CONSTR = None
_CAM_SENS = None
_CAM_PIVOT_POS = None
_CAM_FLUENCY = None
_EMBLEMS_ALPHA_DAMAGED = None
_EMBLEMS_ALPHA_UNDAMAGED = None
_SHADOW_LIGHT_DIR = None
g_offlineMapCreator: Any

class OfflineMapCreator(object):
    mapActivities: Any
    __space: Any
    __cam: Any
    __waitCallback: Any
    __loadingStatus: Any
    __destroyFunc: Any
    __spaceMappingId: Any
    __vEntityId: Any
    __isActive: Any
    __arenaTypeID: Any
    def __init__(self):
        ...
    def create(self, mapName):
        ...
    def destroy(self):
        ...
    def reset(self):
        ...
    def cancel(self):
        ...
    def _clamp(self, minVal, maxVal, val):
        ...
    def Active(self):
        ...
    def SetActive(self, _active):
        ...
    def arenaId(self):
        ...
    @staticmethod
    def __getArenaTypeId(mapName):
        ...
    def __setupCamera(self):
        ...
    def __loadCfg(self, t, mapName):
        ...
