# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/frameworks_common/state_machine/validator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/frameworks_common/state_machine/validator.py
from __future__ import absolute_import
import typing
from . import states as _states
from . import visitor
from .exceptions import StateMachineError
if typing.TYPE_CHECKING:
    from .transitions import BaseTransition
    from . import StateMachine

def _validateTransition(transition, upper=None):
    source = transition.getSource()
    if source is None:
        raise StateMachineError(('{} has no source').format(transition))
    targets = transition.getTargets()
    if not targets:
        raise StateMachineError(('{} has no targets').format(transition))
    if None in targets:
        raise StateMachineError(('{} cannot have a None target').format(transition))
    if visitor.getLCA([source] + targets, upper=upper) is None:
        raise StateMachineError(('States have no LCA in {}').format(transition))
    return


def _validateInitialState(state):
    initial = state.getInitial()
    if not initial:
        raise StateMachineError(('{} has no initial state').format(state))


def _validateState(state, machine):
    if state.isCompound():
        _validateInitialState(state)
    if state.isHistory() and len(state.getTransitions()) > 1:
        raise StateMachineError(('History state {} should have only one transition').format(state))
    if not state.isFinal():
        for transition in state.getTransitions():
            _validateTransition(transition, upper=machine.getParent())


def validate(machine):
    _validateInitialState(machine)
    ids = []
    for state in machine.visitInOrder((lambda item: isinstance(item, _states.State))):
        if state.isMachine():
            if state != machine:
                validate(state)
        else:
            stateID = state.getStateID()
            if stateID:
                if stateID not in ids:
                    ids.append(stateID)
                else:
                    raise StateMachineError(('{} is not unique, each state must have unique ID').format(state))
            _validateState(state, machine)
