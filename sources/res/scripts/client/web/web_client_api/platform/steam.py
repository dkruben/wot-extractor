# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/platform/steam.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/platform/steam.py
from __future__ import absolute_import
import logging, Steam
from constants import DISTRIBUTION_PLATFORM
from web.web_client_api.platform.base import IPlatformWebApi
_logger = logging.getLogger(__name__)

class SteamPlatformWebApi(IPlatformWebApi):

    def getType(self):
        return DISTRIBUTION_PLATFORM.STEAM.value

    def isInited(self):
        return Steam.isInited()

    def isConnected(self):
        return Steam.isInited()

    @staticmethod
    def isOverlayEnabled():
        return Steam.isOverlayEnabled()
