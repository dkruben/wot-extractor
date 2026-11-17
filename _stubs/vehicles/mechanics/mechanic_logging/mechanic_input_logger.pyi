# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_logging/mechanic_input_logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
import weakref as weakref
from functools import partial as partial
import BigWorld as BigWorld
import constants as constants
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.constants import InputLogActions as InputLogActions
from wotdecorators import noexcept as noexcept
import Input as Input
from Input import KeyInputAction as KeyInputAction, InputTriggerPressed as InputTriggerPressed, TriggerEvent as TriggerEvent, InputLayer as InputLayer
from events_containers.components.life_cycle import ILifeCycleComponent as ILifeCycleComponent
from vehicles.mechanics.mechanic_logging.mechanic_interfaces import IMechanicInputLoggingComponent as IMechanicInputLoggingComponent
_logger: Any
_MECHANIC_INPUT_LOGGING_FEATURE_NAME = 'mechanic_input'

class MechanicInputLogger(ContainersListener, IComponentLifeCycleListenerLogic):
    _INPUT_PROFILE_NAME = 'MECHANIC_INPUT_PROFILE'
    _mechanicComponent: Any
    _uiLogger: Any
    __arenaUniqueID: Any
    __vehCD: Any
    def __init__(self, mechanicComponent, *commands):
        ...
    def start(self):
        ...
    def destroy(self):
        ...
    # decorador original: @eventHandler
    def onComponentDestroyed(self, component):
        ...
    # decorador original: @noexcept
    def log(self, triggeredAction):
        ...
