# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/config_schemas/state_machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from constants import IS_CLIENT as IS_CLIENT, IS_CELLAPP as IS_CELLAPP
from dict2model import fields as fields, models as models, schemas as schemas
from dict2model.exceptions import ValidationError as ValidationError
from dict2model.fields import Field as Field
from frameworks_common.state_machine import State as State, StateFlags as StateFlags, StateEvent as StateEvent, StringEventTransition as StringEventTransition, StringEvent as StringEvent
from typing import List as List, Optional as Optional, Iterable as Iterable
timedStateSchema: Any
stateMachineSchema: Any

class TimedStateModel(State, models.Model):
    __slots__: tuple
    _eventDuration: Any
    _callbackId: Any
    _prepareTransitions: Any
    def __init__(self, stateID='', eventDuration=0, transition=None, flags=None):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _onTimeout(self, *_, **__):
        ...
    def getEventDuration(self):
        ...
    def getPreparedTransitions(self):
        ...

class StateMachineModel(models.Model):
    __slots__: tuple
    _states: Any
    def __init__(self, state):
        ...
    def setTimedStateTransition(self, states):
        ...
    def getStates(self):
        ...

class StateFlagField(Field):
    def _serialize(self, incoming, **kwargs):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...
