# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/AccountFunRandomComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/AccountFunRandomComponent.py
from __future__ import absolute_import
import typing, AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from constants import QUEUE_TYPE
from PlayerEvents import g_playerEvents as events
if typing.TYPE_CHECKING:
    from fun_random.gui.prb_control.entities.pre_queue.ctx import FunRandomQueueCtx

class AccountFunRandomComponent(BaseAccountExtensionComponent):

    def enqueueFunRandom(self, ctx):
        self.base.doCmdIntArr(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_ENQUEUE_IN_BATTLE_QUEUE, [
         QUEUE_TYPE.FUN_RANDOM, ctx.getVehicleInventoryID(), ctx.getDesiredSubModeID()])

    def dequeueFunRandom(self):
        if not events.isPlayerEntityChanging:
            self.base.doCmdInt(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_DEQUEUE_FROM_BATTLE_QUEUE, QUEUE_TYPE.FUN_RANDOM)
