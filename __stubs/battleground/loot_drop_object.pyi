# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/loot_drop_object.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import math as math
from collections import namedtuple as namedtuple
import Math as Math
import BigWorld as BigWorld
import CGF as CGF
import AnimationSequence as AnimationSequence
import math_utils as math_utils
from battleground.components import ModelComponent as ModelComponent, SequenceComponent as SequenceComponent
from components_base.component_controller import ComponentController as ComponentController
from math_utils import Easing as Easing
from BombersWing import CompoundBomber as CompoundBomber, BomberDesc as BomberDesc, CurveControlPoint as CurveControlPoint
from Event import Event as Event
from battleground.component_loading import loadComponentSystem as loadComponentSystem, Loader as Loader
from battleground.iself_assembler import ISelfAssembler as ISelfAssembler
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from components_base.component import Component as Component
from components_base.component_descriptor import ComponentDescriptor as ComponentDescriptor, ComponentDescriptorTyped as ComponentDescriptorTyped

class DescendSimulator(Component):
    matrix: Any
    __matrix: Any
    prevTime: Any
    easing: Any
    def __init__(self, yaw, dropPoint, endPoint, descendTime):
        ...
    def tick(self):
        ...

class ParachuteCargo(ComponentController, CallbackDelayer):
    model: Any
    landingAnimation: Any
    descendSimulator: Any
    LANDING_TRIGGER = 'Landed'
    LANDING_ANIMATION_TRIGGER_OFFSET = -0.3
    stopLoading: Any
    __descendTime: Any
    __timeCorrection: Any
    __dropPoint: Any
    def __init__(self, yaw, dropPoint, landingPosition, landingTime, landingDuration):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def tick(self):
        ...
    def __animateLanding(self):
        ...

class DropPlane(Component, CallbackDelayer):
    __dynamicObjectsCache: Any
    __sessionProvider: Any
    TimingConfig: Any
    FLY_TIME_BEFORE_DROP = 20
    FLY_TIME_AFTER_DROP = 10
    UNLOAD_ANIMATION_TIME = 8.0
    FLIGHT_SPEED = 83.33333333333333
    ARRIVAL_VECTOR: Any
    DEPARTURE_VECTOR: Any
    ARRIVAL_TRAJECTORY_INCLINATION: Any
    DEPARTURE_TRAJECTORY_INCLINATION: Any
    flightYaw: Any
    OPEN_CARGO_ANIMATION_TRIGGER = 'OpenCargo'
    CLOSE_CARGO_ANIMATION_TRIGGER = 'CloseCargo'
    __flightYaw: Any
    dropPlane: Any
    prevTime: Any
    def __init__(self, deliveryPoint, dropAltitude, dropTime):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def __openCargo(self):
        ...
    def __closeCargo(self):
        ...
    def tick(self):
        ...

class PlaneLootAirdrop(CallbackDelayer, ISelfAssembler):
    domain = CGF.Domain.ClientEditor
    __dynamicObjectsCache: Any
    __sessionProvider: Any
    FLY_TIME_BEFORE_DROP = DropPlane.FLY_TIME_BEFORE_DROP
    FLY_TIME_AFTER_DROP = DropPlane.FLY_TIME_AFTER_DROP
    DESCEND_TIME = 7.0
    DROP_ALTITUDE = 50
    POST_DELIVERY_CARGO_LIFETIME = 12.0
    parent: Any
    inactiveCargo: Any
    id: Any
    deliveryPosition: Any
    deliveryTime: Any
    onFlightEnd: Any
    def __init__(self, dropID, deliveryPosition, deliveryTime):
        ...
    def start(self, *args, **kwargs):
        ...
    def destroy(self):
        ...
    def __launchPlane(self):
        ...
    def __dropCrate(self):
        ...
    def __onCargoLoad(self, cargo):
        ...
    def __killCargo(self):
        ...
    def __processFlightEnd(self):
        ...

class PlaneLootAirdropSystem(CGF.System):
    DropPlaneIterate: Any
    ParachuteCargoActivate: Any
    ParachuteCargoDeactivate: Any
    ParachuteCargoIterate: Any
    Reactions: Any
    def update(self):
        ...
