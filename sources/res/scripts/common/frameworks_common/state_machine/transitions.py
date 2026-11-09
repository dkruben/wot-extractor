# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/frameworks_common/state_machine/transitions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/frameworks_common/state_machine/transitions.py
from __future__ import absolute_import
import weakref, typing
from enum import IntEnum
from .events import StringEvent
from .node import Node
if typing.TYPE_CHECKING:
    from .events import StateEvent

class TransitionType(IntEnum):
    EXTERNAL = 0
    INTERNAL = 1


class BaseTransition(Node):
    __slots__ = ('__targets', '__priority', '__type')

    def __init__(self, priority=0, transitionType=TransitionType.EXTERNAL):
        super(BaseTransition, self).__init__()
        self.__targets = []
        self.__priority = priority
        self.__type = transitionType

    def __repr__(self):
        return ('{}({}->{}, priority={})').format(self.__class__.__name__, self.getSource(), self.getTargets(), self.getPriority())

    def clear(self):
        del self.__targets[:]
        super(BaseTransition, self).clear()

    def getPriority(self):
        return self.__priority

    def getSource(self):
        return self.getParent()

    def getTargets(self):
        return [target() for target in self.__targets if target() is not None]

    def setTarget(self, state):
        self.__targets.append(weakref.ref(state))

    def getType(self):
        return self.__type

    def execute(self, event):
        raise NotImplementedError


class ConditionTransition(BaseTransition):
    __slots__ = ('__condition', '__invert')

    def __init__(self, condition, invert=False, priority=0):
        super(ConditionTransition, self).__init__(priority=priority)
        self.__condition = condition
        self.__invert = invert

    def clear(self):
        super(ConditionTransition, self).clear()
        self.__condition = None
        return

    def execute(self, event):
        result = self.__condition(event)
        if self.__invert:
            result = not result
        return result


class StringEventTransition(BaseTransition):
    __slots__ = ('__token', )

    def __init__(self, token='', priority=0):
        super(StringEventTransition, self).__init__(priority=priority)
        self.__token = token

    def execute(self, event):
        if isinstance(event, StringEvent):
            return not self.__token or event.token == self.__token
        return False
