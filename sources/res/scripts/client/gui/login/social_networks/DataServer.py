# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/login/social_networks/DataServer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/login/social_networks/DataServer.py
import os, hashlib
from SocketServer import ThreadingMixIn
from Event import Event
from Crypto.Cipher import AES
from Crypto.Util import Counter
from debug_utils import LOG_DEBUG
from py2to3.compat import base64compat
from RequestHandler import RequestHandler
from standalone.login import HttpServer

class DataServer(HttpServer):

    def __init__(self, name):
        HttpServer.__init__(self, name, RequestHandler)
        self.dataReceived = Event()

    def keepData(self, token, spaID, socialNetwork):
        self.dataReceived(token, spaID, socialNetwork)

    def _logStatus(self):
        LOG_DEBUG(self._currentStatus)


class EncryptingDataServer(DataServer):

    def __init__(self, name):
        DataServer.__init__(self, name)
        self._tokenSecret = hashlib.sha1(os.urandom(128)).hexdigest()[:16]

    def keepData(self, token, spaID, socialNetwork):
        cipher = AES.new(self._tokenSecret, AES.MODE_CTR, counter=Counter.new(128))
        token = cipher.decrypt(base64compat.urlsafe_b64decode(token))
        DataServer.keepData(self, token, spaID, socialNetwork)

    @property
    def tokenSecret(self):
        return self._tokenSecret


class ThreadedDataServer(ThreadingMixIn, DataServer):

    def __init__(self, name):
        DataServer.__init__(self, name)


class EncryptingThreadedDataServer(ThreadingMixIn, EncryptingDataServer):

    def __init__(self, name):
        EncryptingDataServer.__init__(self, name)
