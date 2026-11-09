# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/queues/LimitedThroughputQueue.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/queues/LimitedThroughputQueue.py
from __future__ import absolute_import
from past.builtins import xrange
import BigWorld

class LimitedThroughputQueue:

    def __init__(self, actionsPerSecond, maxActionsPerBatch=1):
        self.__queue = []
        self.__actionsPerSecond = actionsPerSecond
        self.__maxActionsPerBatch = maxActionsPerBatch
        self.__timerID = 0

    def scheduleAction(self, action):
        self.__queue.append(action)
        self._startJob()

    def _startJob(self):
        if self.__timerID != 0:
            return
        self.__timerID = BigWorld.addTimer(self._job, 0, 1.0 / self.__maxActionsPerBatch)

    def _stopJob(self):
        if self.__timerID == 0:
            return
        BigWorld.delTimer(self.__timerID)
        self.__timerID = 0

    def _job(self, timerID, _=0):
        for _ in xrange(0, self.__actionsPerSecond // self.__maxActionsPerBatch):
            action = self.__queue.pop()
            action()
            if len(self.__queue) == 0:
                self._stopJob()
                break

    @property
    def actionsPerSecond(self):
        return self.__actionsPerSecond
