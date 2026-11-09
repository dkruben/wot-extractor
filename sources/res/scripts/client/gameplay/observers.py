# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gameplay/observers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gameplay/observers.py
from __future__ import absolute_import
from collections import defaultdict
from frameworks_common.state_machine import BaseStateObserver
from gameplay.blockers import BlockingStateMixin

class BlockingStateClearObserver(BaseStateObserver):

    def __init__(self):
        self.__clearIDsToBlockingStates = defaultdict(list)

    def clear(self):
        self.__clearIDsToBlockingStates = defaultdict(list)

    def isObservingState(self, state):
        return True

    def onEnterState(self, state, event):
        if event is not None or self.__clearIDsToBlockingStates:
            return
        machine = state.getMachine()
        for child in machine.getRecursiveChildrenStates():
            if isinstance(child, BlockingStateMixin):
                self.__clearIDsToBlockingStates[child.blockerClearLifetimeStateID].append(child)

        return

    def onExitState(self, state, event):
        for blockerState in self.__clearIDsToBlockingStates.get(state.getStateID(), []):
            blockerState.clearBlockers()
