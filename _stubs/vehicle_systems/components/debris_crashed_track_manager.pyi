# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/debris_crashed_track_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from builtins import range as range
from future.utils import viewitems as viewitems
import CGF as CGF
import Vehicular as Vehicular
import math_utils as math_utils
from constants import IS_CGF_DUMP as IS_CGF_DUMP, IS_EDITOR as IS_EDITOR
from items.components.component_constants import MAIN_TRACK_PAIR_IDX as MAIN_TRACK_PAIR_IDX
from items.vehicle_items import CHASSIS_ITEM_TYPE as CHASSIS_ITEM_TYPE
from vehicle_systems import tankStructure as tankStructure
from vehicle_systems.components.CrashedTracks import CrashedTracksController as CrashedTracksController
from vehicle_systems.components.vehicle_pickup_component import VehiclePickupComponent as VehiclePickupComponent
from vehicle_systems.components.debris_crashed_track_component import DebrisCrashedTrackComponent as DebrisCrashedTrackComponent, NodeRemapperComponent as NodeRemapperComponent
from vehicle_systems.tankStructure import TankSoundObjectsIndexes as TankSoundObjectsIndexes
from functools import partial as partial
from CustomEffectManager import CustomEffectManager as CustomEffectManager
_logger: Any

class DebrisCrashedTrackSystem(CGF.System):
    RTPC_OUTER_TRACK_STATE = 'RTPC_ext_treads_outer'
    DEBRIS_MAX_LIFETIME = 10
    Activated: Any
    Deactivated: Any
    PickupActivated: Any
    PickupDeactivated: Any
    TrackDebrisAccess: Any
    CompositeTrackAccess: Any
    WheelsAccess: Any
    TrackAccess: Any
    SuspensionAccess: Any
    NodeAccess: Any
    AuditionAccess: Any
    CrashedTracksControllerAccess: Any
    EffectActivated: Any
    EffectDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def __forEachValidTrackGameObject(self, appearance, predicate):
        ...
    def __removePhysicalDestroyedTrack(self, debrisTrackAccess, trackGO):
        ...
    def __removePhysicalDestroyedTracks(self, appearance, debrisTrackAccess):
        ...
    def __recreatePhysicalDestroyedTrack(self, queue, compositeTrackAccess, debrisTrackAccess, tracksAccess, trackGO):
        ...
    def __recreatePhysicalDestroyedTracks(self, appearance, queue, compositeTrackAccess, debrisTrackAccess, tracksAccess):
        ...
    def __switchVehicleTrackVisibility(self, track, debris, isVisible, wheelsAccess, tracksAccess, compositeTrackAccess, debrisTrackAccess, suspensionAccess):
        ...
    def __generateDestructionEffect(self, debris):
        ...
    def __remapNodes(self, debris, queue, remapperAccess):
        ...
    def __unmapNodes(self, debris, queue, remapperAccess):
        ...
    def __adjustTrackAudition(self, amountOfBrokenTracks, appearanceGo, auditionAccess):
        ...
    def __createDebris(self, track, debrisComponent, queue, tracksAccess):
        ...
