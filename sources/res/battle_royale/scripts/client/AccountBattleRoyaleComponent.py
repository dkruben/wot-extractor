# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/AccountBattleRoyaleComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/AccountBattleRoyaleComponent.py
from __future__ import absolute_import
import logging, BattleRoyaleConstants as brc, AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from battle_royale.gui.constants import BattleRoyaleSubMode
from battle_royale.gui.prb_control.entities.regular.pre_queue.entity import BRQueueCtx
from PlayerEvents import g_playerEvents as events
from constants import QUEUE_TYPE
_logger = logging.getLogger(__name__)

class AccountBattleRoyaleComponent(BaseAccountExtensionComponent):

    def setBrCoin(self, amount, callback=None):
        _logger.debug("set battle royale coin amount: '%r'", amount)
        self.entity._doCmdIntStr(brc.CMD_BATTLE_ROYALE_OPERATE_BRCOIN, amount, '', callback)

    def enqueueBattleRoyale(self, ctx):
        if not events.isPlayerEntityChanging:
            self.base.doCmdIntArr(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_ENQUEUE_IN_BATTLE_QUEUE, [
             QUEUE_TYPE.BATTLE_ROYALE, ctx.getVehicleInventoryID(),
             int(ctx.getCurrentSubModeID() == BattleRoyaleSubMode.SOLO_DYNAMIC_MODE_ID)])

    def dequeueBattleRoyale(self):
        if not events.isPlayerEntityChanging:
            self.base.doCmdInt(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_DEQUEUE_FROM_BATTLE_QUEUE, QUEUE_TYPE.BATTLE_ROYALE)
