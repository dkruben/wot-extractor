# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/arena_components/comp7_core_equipment_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from collections import defaultdict as defaultdict
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
import math_utils as math_utils
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from helpers import dependency as dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import List as List
_logger: Any

class Comp7CoreEquipmentComponent(ClientArenaComponent):
    __sessionProvider: Any
    _AOE_HEAL_EFFECT = None
    __effects: Any
    def __init__(self, componentSystem):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def __clear(self):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __updateAoeEffect(self, eventID, vehicleID, value, effectClass):
        ...

class _Effect(object):
    __sessionProvider: Any
    _dynObjectsCache: Any
    _parent: Any
    _vehicle: Any
    _prefab: Any
    __destroyed: Any
    def __init__(self, parent, vehicle):
        ...
    @property
    def _modeController(self):
        ...
    @property
    def radius(self):
        ...
    def start(self):
        ...
    def destroy(self):
        ...
    @classmethod
    def isVisible(cls, vehicle, value, checkTeam=True):
        ...
    def _load(self):
        ...
    def _onLoaded(self, objects, queue):
        ...
    def _getPath(self):
        ...
    def _getParent(self):
        ...
    def _getPosition(self):
        ...
    @classmethod
    def _getDynObjectsCacheConfig(cls):
        ...
    def _updateRadius(self, root, queue):
        ...

class _AoeHealEffect(_Effect):
    def _getPath(self):
        ...
    def _updateRadius(self, root, queue):
        ...
