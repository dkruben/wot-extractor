# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lobby_ctx_notifiers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lobby_ctx_notifiers.py
from __future__ import absolute_import
from collections import namedtuple
from gui import SystemMessages
from gui.impl import backport
from gui.shared.notifications import NotificationPriorityLevel
NotifySysMessages = namedtuple('NotifySysMessages', 'resID, priority, type')
NotifySysMessages.__new__.__defaults__ = (
 None, NotificationPriorityLevel.MEDIUM, SystemMessages.SM_TYPE.Information)

class BaseNotifier(object):
    __slots__ = ()

    def getPath(self):
        raise NotImplementedError


class SimpleSysMessageNotifier(BaseNotifier):
    __slots__ = ('__states', '__path')

    def __init__(self, path, states):
        self.__path = path
        self.__states = states

    def __call__(self, nextValue, currentValue):
        if (
         currentValue, nextValue) in self.__states:
            msg = self.__states[(currentValue, nextValue)]
            SystemMessages.pushMessage(backport.text(msg.resID), priority=msg.priority, type=msg.type)

    def getPath(self):
        return self.__path
