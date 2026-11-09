# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/gift_system/requesters/history_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/requesters/history_requester.py
import BigWorld
from adisp import adisp_async
from constants import REQUEST_COOLDOWN
from gui.gift_system.requesters.base_requester import GiftSystemBaseRequester

class GiftSystemHistoryRequester(GiftSystemBaseRequester):
    __slots__ = ()

    def _getInvokeDelay(self):
        return REQUEST_COOLDOWN.SYNC_GIFTS

    @adisp_async
    def _doExternalRequest(self, reqEventIds, callback):
        BigWorld.player().giftSystem.requestGiftsHistory(reqEventIds, callback)
