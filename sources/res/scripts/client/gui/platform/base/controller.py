# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/base/controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/base/controller.py
import typing, wg_async
from BWUtil import AsyncReturn
from gui.platform.base import logger
from gui.platform.base.requester import PlatformRequester
from gui.platform.base.settings import REQUEST_TIMEOUT
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.platform.controller import IPlatformRequestController
if typing.TYPE_CHECKING:
    from gui.platform.base.request import Params

class PlatformRequestController(IPlatformRequestController):
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self):
        super(PlatformRequestController, self).__init__()
        self._requester = None
        self._logger = logger.getWithContext(instance=self)
        return

    def init(self):
        self.connectionMgr.onConnected += self._start
        self.connectionMgr.onDisconnected += self._stop
        self._logger.debug('Initialized.')

    def fini(self):
        self.connectionMgr.onConnected -= self._start
        self.connectionMgr.onDisconnected -= self._stop
        self._logger.debug('Destroyed.')

    @wg_async.wg_async
    def _request(self, params, timeout=REQUEST_TIMEOUT, waitingID=None):
        if self._requester is None:
            self._logger.debug('Not started.')
            response = params.response.createServiceNotStarted()
        else:
            response = yield self._requester.request(params, timeout=timeout, waitingID=waitingID)
        raise AsyncReturn(response)
        return

    def _start(self):
        self._requester = PlatformRequester()
        self._logger.debug('Started.')

    def _stop(self):
        if self._requester:
            self._requester.clear()
        self._requester = None
        self._logger.debug('Stopped.')
        return
