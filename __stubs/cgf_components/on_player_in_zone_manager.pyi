# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/on_player_in_zone_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from collections import OrderedDict as OrderedDict, defaultdict as defaultdict, namedtuple as namedtuple
from functools import partial as partial
from typing import Optional as Optional, List as List
from Triggers import AreaTriggerComponent as AreaTriggerComponent
from Vehicular import OnPlayerInZoneComponent as OnPlayerInZoneComponent
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import isPlayerAvatar as isPlayerAvatar
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
_ActivePrefabInfo: Any

class Vehicle(object):
    ...

class OnPlayerInZoneSystem(CGF.System):
    PlayerZoneActivated: Any
    PlayerZoneDeactivated: Any
    PlayerZoneAccess: Any
    VehicleAccess: Any
    Reactions: Any
    __prefabPathMap: Any
    __activePrefab: Any
    def update(self):
        ...
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def onAdded(self, component, trigger):
        ...
    def onRemoved(self, component, trigger):
        ...
    def __onPrefabLoaded(self, vehicleId, prefabPath, objects, queue):
        ...
    def __updatePlayerPrefab(self):
        ...
    def __removeActivePrefab(self):
        ...
    def __onEnterReaction(self, who, where):
        ...
    def __onExitReaction(self, who, where):
        ...
    def __onAvatarReady(self):
        ...
    def __onAvatarVehicleChanged(self):
        ...
    def __onVehicleLeaveWorld(self, vehicle):
        ...

def _isAvatarReady():
    ...
