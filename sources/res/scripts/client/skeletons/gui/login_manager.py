# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/login_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/login_manager.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from constants import WGC_PUBLICATION

class ILoginManager(object):
    onConnectionInitiated = None
    onConnectionRejected = None

    @property
    def servers(self):
        raise NotImplementedError

    @property
    def wgcAvailable(self):
        raise NotImplementedError

    def getWgcPublication(self):
        raise NotImplementedError

    @property
    def isWgcSteam(self):
        raise NotImplementedError

    def tryPrepareWGCLogin(self):
        raise NotImplementedError

    def checkWgcCouldRetry(self, loginStatus):
        raise NotImplementedError

    def addOnWgcErrorListener(self, listener):
        raise NotImplementedError

    def removeOnWgcErrorListener(self, listener):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def initiateLogin(self, email, password, serverName, isSocialToken2Login, rememberUser):
        raise NotImplementedError

    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        raise NotImplementedError

    def tryWgcLogin(self, serverName=None):
        raise NotImplementedError

    def stopWgc(self):
        raise NotImplementedError

    def initiateRelogin(self, login, token2, serverName):
        raise NotImplementedError

    def getPreference(self, key):
        raise NotImplementedError

    def clearPreferences(self):
        raise NotImplementedError

    def clearToken2Preference(self):
        raise NotImplementedError

    def writePreferences(self):
        raise NotImplementedError

    def writePeripheryLifetime(self):
        raise NotImplementedError

    @staticmethod
    def getAvailableSocialNetworks():
        raise NotImplementedError
