# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/gift_system/requesters/state_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/requesters/state_requester.py
from adisp import adisp_async, adisp_process
from gui.gift_system.requesters.base_requester import GiftSystemBaseRequester
from gui.wgcg.gift_system.contexts import GiftSystemStateCtx
from helpers import dependency
from helpers.time_utils import ONE_MINUTE
from skeletons.gui.web import IWebController
_WGCG_AVAILABILITY = 2
_WGGG_AVAILABILITY = ONE_MINUTE

class GiftSystemWebStateRequester(GiftSystemBaseRequester):
    __slots__ = ()
    __webController = dependency.descriptor(IWebController)

    def _getInvokeDelay(self):
        if self.__webController.isAvailable():
            return _WGGG_AVAILABILITY
        return _WGCG_AVAILABILITY

    @adisp_async
    @adisp_process
    def _doExternalRequest(self, reqEventIds, callback):
        if not self.__webController.isAvailable():
            callback((False, {}))
            return
        requestCtx = GiftSystemStateCtx(reqEventIds)
        result = yield self.__webController.sendRequest(requestCtx)
        callback((result.isSuccess(), requestCtx.getDataObj(result.data) if result.isSuccess() else {}))
