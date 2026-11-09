# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/wgnp/base/controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/base/controller.py
import typing, wg_async
from BWUtil import AsyncReturn
from gui.platform.base.controller import PlatformRequestController
from gui.platform.base.settings import REQUEST_TIMEOUT
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.platform.wgnp_controllers import IWGNPRequestController
if typing.TYPE_CHECKING:
    from gui.platform.base.request import Params
    from helpers.server_settings import _Wgnp

class WGNPRequestController(PlatformRequestController, IWGNPRequestController):
    lobbyContext = dependency.descriptor(ILobbyContext)

    @property
    def settings(self):
        return self.lobbyContext.getServerSettings().wgnp

    @wg_async.wg_async
    def _request(self, params, timeout=REQUEST_TIMEOUT, waitingID=None):
        if not self.settings.isEnabled():
            self._logger.debug('WGNP disabled.')
            response = params.response.createServiceDisabled()
        else:
            response = yield super(WGNPRequestController, self)._request(params, timeout=timeout, waitingID=waitingID)
        raise AsyncReturn(response)
