# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/default_appearance_cache_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
import CGF as CGF
from common_tank_structure import VehicleAppearanceCacheInfo as VehicleAppearanceCacheInfo
from gui.battle_control.arena_info.interfaces import IAppearanceCacheController as IAppearanceCacheController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from skeletons.vehicle_appearance_cache import IAppearanceCache as IAppearanceCache
from helpers import dependency as dependency
from soft_exception import SoftException as SoftException
from wg_async import wg_async as wg_async
_logger: Any

class DefaultAppearanceCacheController(IAppearanceCacheController):
    _appearanceCache: Any
    _arena: Any
    _spaceLoaded: Any
    _precacheFunc: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def addVehicleInfo(self, vo, arenaDP):
        ...
    def updateVehiclesInfo(self, updated, arenaDP):
        ...
    def getAppearance(self, vId, vInfo, callback=None, strCD=None, needLoad=True):
        ...
    def reloadAppearance(self, vId, vInfo, callback=None, strCD=None, oldStrCD=None):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _setCacheAppearanceFunc(self):
        ...
    def _precache(self, vehiclesInfo, groupIDs=None):
        ...
    def _cacheAllVehicles(self, vehiclesInfo, _=None):
        ...
    def _cachePlayerGroupVehicles(self, vehiclesInfo, groupIDs=None):
        ...
    def invalidateVehiclesInfo(self, arenaDP):
        ...
    # decorador original: @wg_async
    def _onPlayerGroupsUpdated(self, vIds):
        ...
    def __cacheVehicle(self, vId, vInfo):
        ...
