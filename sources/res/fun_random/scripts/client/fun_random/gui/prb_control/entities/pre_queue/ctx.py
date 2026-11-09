# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/ctx.py
from __future__ import absolute_import
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx, JoinPreQueueModeCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryID', 'vInvID'), ('getDesiredSubModeID',
                                                               'subModeID'))
class FunRandomQueueCtx(QueueCtx):
    __slots__ = ('__desiredSubModeID', '__vInventoryID')

    def __init__(self, vInventoryID, desiredSubModeID, waitingID=''):
        super(FunRandomQueueCtx, self).__init__(entityType=QUEUE_TYPE.FUN_RANDOM, waitingID=waitingID)
        self.__desiredSubModeID = desiredSubModeID
        self.__vInventoryID = vInventoryID

    def getDesiredSubModeID(self):
        return self.__desiredSubModeID

    def getVehicleInventoryID(self):
        return self.__vInventoryID


@ReprInjector.withParent(('getDesiredSubModeID', 'desiredSubModeID'))
class JoinFunPreQueueModeCtx(JoinPreQueueModeCtx):
    __slots__ = ('__desiredSubModeID', )

    def __init__(self, queueType, desiredSubModeID, flags=FUNCTIONAL_FLAG.UNDEFINED, waitingID=''):
        super(JoinFunPreQueueModeCtx, self).__init__(queueType=queueType, flags=flags, waitingID=waitingID)
        self.__desiredSubModeID = desiredSubModeID

    def getDesiredSubModeID(self):
        return self.__desiredSubModeID
