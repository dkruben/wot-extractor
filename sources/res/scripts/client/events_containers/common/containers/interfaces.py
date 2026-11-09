# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/common/containers/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/common/containers/interfaces.py
from __future__ import absolute_import
import typing

class IClientEventsContainer(object):
    onEventsContainerDestroy = None

    @property
    def hasListeners(self):
        raise NotImplementedError

    def destroy(self):
        pass

    def attachCFGEvents(self):
        pass

    def debugEvents(self):
        pass

    def lateSubscribe(self, listener):
        listener.subscribeTo(self)

    def unsubscribe(self, listener):
        listener.unsubscribeFrom(self)


class IClientEventsContainerListener(object):

    def subscribeTo(self, events):
        raise NotImplementedError

    def unsubscribeFrom(self, events):
        raise NotImplementedError

    def lateSubscribeTo(self, events):
        raise NotImplementedError
