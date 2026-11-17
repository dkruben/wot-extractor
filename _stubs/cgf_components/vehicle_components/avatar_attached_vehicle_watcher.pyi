# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/vehicle_components/avatar_attached_vehicle_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import typing as typing
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
import CGF as CGF
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from Event import EventsSubscriber as EventsSubscriber
from Avatar import Avatar as Avatar
from Event import SafeEvent as SafeEvent
VehAccessorType: Any
_logger: Any

class Vehicle(object):
    ...

# decorador original: @enum.unique
class ActiveForTypes(enum.IntEnum):
    SELF = 0
    OTHERS = 1
    TEAMMATES = 2
    ENEMIES = 3

# decorador original: @registerComponent
class AvatarAttachedVehicleWatcherComponent(object):
    category = 'Vehicle'
    editorTitle = 'Avatar Attached Vehicle Watcher'
    domain = CGF.Domain.ClientEditor
    activeFor: Any
    _subscriber: Any
    def __init__(self):
        ...
    def subscribe(self, event, callback):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def __repr__(self):
        ...

class AvatarAttachedVehicleWatcherSystem(CGF.System):
    WatcherActivated: Any
    WatcherDeactivated: Any
    WatcherRemoved: Any
    VehicleAccess: Any
    Reactions: Any
    def update(self):
        ...
    def _onActivated(self, go, component, vehAccess):
        ...
    def _updateHierarchy(self, go, vehGO, activeFor):
        ...
    def _deactivate(self, go):
        ...
    def _activate(self, go):
        ...
    @staticmethod
    def _shouldBeActive(attachedVehicle, currentVehicle, activeFor):
        ...
