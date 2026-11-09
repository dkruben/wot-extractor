# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWDeathZone.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
from shared_utils import nextTick as nextTick
from PlayerEvents import g_playerEvents as g_playerEvents
from LimitedVisibilityEntity import LimitedVisibilityEntity as LimitedVisibilityEntity
from StaticDeathZone import DeathZoneMarkerHandler as DeathZoneMarkerHandler
from halloween_dyn_object_cache import getModel as getModel
_TICK_UPDATE_TIME = 0

class HWDeathZone(LimitedVisibilityEntity):
    onResizeDeathZone: Any
    onActiveChanged: Any
    onMaskAdded: Any
    _tickTimerID: Any
    _marker: Any
    _vehiclesInside: Any
    _serverTime: Any
    _position: Any
    _zoneSize: Any
    _rotation: Any
    _transformPosPerSec: Any
    _transformSizePerSec: Any
    _transformRotationPerSec: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def _onAvatarReady(self):
        ...
    @property
    def position(self):
        ...
    @property
    def zoneSize(self):
        ...
    @property
    def rotation(self):
        ...
    @property
    def visual(self):
        ...
    def set_isActive(self, _):
        ...
    def set_requestedTransform(self, _):
        ...
    def set_vehiclesInside(self, _):
        ...
    @property
    def udoGuid(self):
        ...
    @property
    def masks(self):
        ...
    @property
    def polygonCenter(self):
        ...
    @property
    def isAvatarReady(self):
        ...
    def getDimensions(self):
        ...
    def getClosestPoint(self, pos, searchRadius):
        ...
    def getBorderModel(self, borderID):
        ...
    def _transform(self, requested=False):
        ...
    def _resize(self, position, zoneSize, rotation, force=False):
        ...
    def _createMarker(self):
        ...
    def _removeMarker(self):
        ...
    def _tick(self):
        ...
    def _clearTickTimer(self):
        ...
