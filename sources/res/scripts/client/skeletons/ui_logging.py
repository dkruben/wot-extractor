# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/ui_logging.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/ui_logging.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from uilogging.types import FeatureType, GroupType, ActionType, LogLevelType

class IUILoggingCore(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def isFeatureEnabled(self, feature):
        raise NotImplementedError

    def log(self, feature, group, action, loglevel, **params):
        raise NotImplementedError

    def logImmediately(self, feature, group, action, loglevel, **params):
        raise NotImplementedError

    def ensureSession(self):
        raise NotImplementedError

    def start(self, ensureSession=False):
        raise NotImplementedError

    def send(self):
        raise NotImplementedError


class IUILoggingListener(object):

    def fini(self):
        raise NotImplementedError
