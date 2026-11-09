# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_state_machine/registrar.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_state_machine/registrar.py
from __future__ import absolute_import
import inspect, logging, types
from .actions_base import ActionBase
from .transitions_base import TransitionBase
from constants import IS_DEVELOPMENT
__all__ = [
 'StateActionsRegistrar', 'TransitionsRegistrar']
_logger = logging.getLogger(__name__)

def findClassesInModule(module, baseCls):
    return list(value for key, value in inspect.getmembers(module, inspect.isclass) if issubclass(value, baseCls) and value is not baseCls and inspect.getmodule(value) is module and (not value.isDevOnly() or IS_DEVELOPMENT))


class StateActionsRegistrar(object):

    def __init__(self):
        self._domainActions = set()

    def regActionsFromModule(self, module):
        for action in findClassesInModule(module, ActionBase):
            if action in self._domainActions:
                _logger.error('Action already registered: %s', action.__name__)
            else:
                self._domainActions.add(action)

    def getActions(self):
        return self._domainActions


class TransitionsRegistrar(object):

    def __init__(self):
        self._transitions = set()

    def regTransitionsFromModule(self, module):
        for transition in findClassesInModule(module, TransitionBase):
            if transition in self._transitions:
                _logger.error('Transition already registered: %s', transition.__name__)
            else:
                self._transitions.add(transition)

    def getTransitions(self):
        return self._transitions
