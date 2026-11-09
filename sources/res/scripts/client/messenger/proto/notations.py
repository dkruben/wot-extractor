# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/notations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/notations.py
from __future__ import absolute_import
from debug_utils import LOG_NOTE
from messenger import g_settings
from messenger.m_constants import PROTO_TYPE_NAMES

class _profile(object):

    def __init__(self, protoType, log=True):
        super(_profile, self).__init__()
        self._protoType = protoType
        self._doLog = log

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            if not self.isEnabled():
                if self._doLog:
                    self.log(func.__name__)
            else:
                func(*args, **kwargs)

        return wrapper

    def isEnabled(self):
        raise NotImplementedError

    def log(self, name):
        raise NotImplementedError


class contacts(_profile):

    def isEnabled(self):
        return g_settings.server.useToShowContacts(self._protoType)

    def log(self, name):
        LOG_NOTE(('Routine {0} is blocked. Client can not send request on changing contacts by {1} protocol').format(name, PROTO_TYPE_NAMES[self._protoType]))
