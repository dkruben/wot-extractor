# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/rocket_acceleration_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
import BigWorld as BigWorld
from functools import partial as partial
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from GameplayDebug import DebugTextComponent as DebugTextComponent
from constants import IS_CLIENT as IS_CLIENT, HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from constants import ROCKET_ACCELERATION_STATE as ROCKET_ACCELERATION_STATE
from GenericComponents import VSEComponent as VSEComponent
_logger: Any

class RocketAccelerationController(object):
    ...

class SoundEvents(object):
    ROCKET_ACCELERATION_READY = 'ev_rocket_accel_ready'
    ROCKET_ACCELERATION_ACTIVE_PC = 'ev_rocket_accel_start_PC'
    ROCKET_ACCELERATION_ACTIVE_NPC = 'ev_rocket_accel_start_NPC'
    ROCKET_ACCELERATION_STOP_PC = 'ev_rocket_accel_stop_PC'
    ROCKET_ACCELERATION_STOP_NPC = 'ev_rocket_accel_stop_NPC'
    ROCKET_ACCELERATION_DISABLE = 'ev_rocket_accel_disable'
    ROCKET_ACCELERATION_EMPTY = 'ev_rocket_accel_empty'

# decorador original: @registerComponent
class RocketAccelerationTerrainEffect(object):
    category = 'Rocket Accelerator'
    editorTitle = 'Rocket Accelerator Terrain Effect'
    domain = CGF.Domain.Client
    snow: Any
    sand: Any
    ground: Any
    stone: Any

# decorador original: @registerComponent
class RocketAccelerationStateListener(object):
    category = 'Rocket Accelerator'
    editorTitle = 'Rocket Accelerator State Listener'
    domain = CGF.Domain.Client
    vseComponent: Any
    start: Any
    idle: Any
    end: Any
    sound_l: Any
    sound_r: Any
    startDuration: Any
    endDuration: Any
    soundReady: Any
    soundActivePC: Any
    soundActiveNPC: Any
    soundStopPC: Any
    soundStopNPC: Any
    soundDisable: Any
    soundEmpty: Any

class RocketAccelerationSystem(CGF.System):
    AccelerationActivated: Any
    AccelerationDeactivated: Any
    RocketAccelerationControllerAccess: Any
    VSEComponentAccess: Any
    Reactions: Any
    def update(self):
        ...

class RocketAccelerationSystemDebug(CGF.System):
    ListenerActivated: Any
    ListenerDeactivated: Any
    RocketAccelerationControllerAccess: Any
    DebugTextAccess: Any
    Reactions: Any
    __texts: Any
    __listeners: Any
    def __init__(self):
        ...
    def commonUpdate(self):
        ...
    def periodUpdate(self):
        ...
    def onStateUpdate(self, root, status, _):
        ...
    def __updateState(self, root, value, status):
        ...
    def __updateText(self, text, value, count):
        ...
    def __updateTextWithDuration(self, text, value, count, end):
        ...
    def __setupDebugStateHandling(self, root, provider, queue):
        ...
