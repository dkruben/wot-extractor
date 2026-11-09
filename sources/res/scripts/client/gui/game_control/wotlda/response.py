# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/wotlda/response.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/wotlda/response.py
from __future__ import absolute_import
from http import client as httplib
from typing import Dict, Optional, TYPE_CHECKING
from gui.game_control.wotlda.constants import LAST_UPDATE_TIMESTAMP, SupportedWotldaLoadoutType
if TYPE_CHECKING:
    from gui.shared.utils.requesters.abstract import Response

class WotldaResponse(object):

    def __init__(self, response):
        self._response = response
        self._exception = None
        return

    def getData(self):
        if self.isSuccess():
            return self._response.getData()
        return {}

    def setException(self, exception):
        self._exception = exception

    def isSuccess(self):
        if self._response:
            return self._response.getExtraCode() == httplib.OK
        return False

    def isNotModified(self):
        if self._response:
            return self._response.getExtraCode() == httplib.NOT_MODIFIED
        return False

    def isServiceUnavailable(self):
        if self._response:
            return self._response.getExtraCode() == httplib.SERVICE_UNAVAILABLE
        return True

    def hasRequestFailed(self):
        return self._exception or not self.isSuccess() and not self.isNotModified()

    def getLoadoutsByType(self, loadoutType):
        return self.getData().get(loadoutType, {})

    def getTimestamp(self):
        return self.getData().get(LAST_UPDATE_TIMESTAMP, 0)
