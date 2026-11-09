# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/base/pre_queue/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/ctx.py
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE, REQUEST_TYPE
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

class _PreQueueRequestCtx(PrbCtrlRequestCtx):

    def __init__(self, **kwargs):
        super(_PreQueueRequestCtx, self).__init__(ctrlType=CTRL_ENTITY_TYPE.PREQUEUE, **kwargs)


class QueueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.QUEUE


class DequeueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.DEQUEUE


class JoinPreQueueModeCtx(_PreQueueRequestCtx):

    def __init__(self, queueType, flags=FUNCTIONAL_FLAG.UNDEFINED, waitingID=''):
        super(JoinPreQueueModeCtx, self).__init__(entityType=queueType, flags=flags, waitingID=waitingID)

    def getID(self):
        return 0


@ReprInjector.withParent(('getWaitingID', 'waitingID'))
class LeavePreQueueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.LEAVE
