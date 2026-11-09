# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_post_progression/models/iterators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_post_progression/models/iterators.py
import typing
from collections import deque
if typing.TYPE_CHECKING:
    from gui.veh_post_progression.models.progression import PostProgressionItem

class UnorederdStepsIterator(object):
    __slots__ = ('_postProgression', '_tree')

    def __init__(self, postProgression):
        self._postProgression = postProgression
        self._tree = postProgression.getRawTree()

    def __iter__(self):
        return (self._postProgression.getStep(stepID) for stepID in self._tree.steps.keys())


class OrderedStepsIterator(UnorederdStepsIterator):
    __slots__ = ('__fifo', '__visited')

    def __init__(self, postProgression):
        super(OrderedStepsIterator, self).__init__(postProgression)
        self.__fifo = deque((self._tree.rootStep,))
        self.__visited = set()

    def __iter__(self):
        return self

    def next(self):
        if not self.__fifo:
            raise StopIteration
        step = self._postProgression.getStep(self.__fifo.popleft())
        self.__visited.add(step.stepID)
        self.__fifo.extend(self._getOrderedUnlocks(step.getNextStepIDs()))
        return step

    def _getOrderedUnlocks(self, unlocks):
        return tuple(set(unlocks).difference(self.__visited))
