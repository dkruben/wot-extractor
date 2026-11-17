# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StationaryReloadController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import math as math
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from constants import STATIONARY_RELOAD_STATE as STATIONARY_RELOAD_STATE, GUN_LOCK_REASONS as GUN_LOCK_REASONS
from events_handler import eventHandler as eventHandler
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState, AmmoShootPossibility as AmmoShootPossibility
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from messenger_common_chat2 import messageArgs as messageArgs
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents, createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent, IMechanicState as IMechanicState
from typing import Optional as Optional, Any as Any
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents

class StationaryReloadAmmoState(DefaultComponentAmmoState):
    __sessionProvider: _Any
    __state: _Any
    __baseTime: _Any
    __timeLeft: _Any
    def __init__(self, state, baseTime, timeLeft):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    @property
    def stationaryReloadState(self):
        ...
    @property
    def stationaryBaseTime(self):
        ...
    @property
    def stationaryTimeLeft(self):
        ...
    def isReloadingBlocked(self):
        ...
    def getShootPossibility(self, _):
        ...
    def getSpecialReloadMessage(self):
        ...

# base nao representavel no stub: namedtuple(...)
class StationaryReloadModeState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    @property
    def sequenceTimeLeft(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class StationaryReloadController(VehicleDynamicComponent, IGunMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    DEFAULT_AMMO_STATE: _Any
    DEFAULT_MODE_STATE: _Any
    __mechanicPrefabSpawner: _Any
    __commandsEvents: _Any
    __statesEvents: _Any
    def __init__(self):
        ...
    def set_status(self, _):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def commandsEvents(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getAmmoState(self):
        ...
    def getMechanicState(self):
        ...
    def onDestroy(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    def tryActivate(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
