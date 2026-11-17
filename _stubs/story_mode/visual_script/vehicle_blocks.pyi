# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/visual_script/vehicle_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import List as List, TYPE_CHECKING as TYPE_CHECKING
import weakref as weakref
from story_mode.visual_script.enums import SMAwarenessStateEnum as SMAwarenessStateEnum
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.tunable_event_block import TunableEventBlock as TunableEventBlock
from visual_script_client.player_blocks import PlayerEventMeta as PlayerEventMeta
from visual_script_client.vehicle_common import TunablePlayerVehicleEventBlock as TunablePlayerVehicleEventBlock
from Math import Vector3 as Vector3
import Vehicle as Vehicle

class OnPlayerAwarenessStateChange(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _state: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onAwarenessStateChanged(self, state):
        ...

class OnSMReconAbilityActivated(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _index: Any
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onSMReconAbilityActivated(self, isActivated):
        ...

class OnSMReconAbilitySpottedVehicles(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _vehicleIDs: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onSMReconAbilitySpottedVehicles(self, spottedVehiclesIDs):
        ...

class OnSMDistractionAbilityActivated(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _vehicles: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onSMDistractionAbilityActivated(self, spottedVehicles):
        ...

class OnSMAbilityWrongPoint(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _point: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onSMAbilityWrongPoint(self, point):
        ...
