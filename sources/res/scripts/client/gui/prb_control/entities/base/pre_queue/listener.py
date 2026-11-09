# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/base/pre_queue/listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/listener.py
from gui.prb_control.entities.base.listener import IPrbListener

class IPreQueueListener(IPrbListener):

    def onEnqueued(self, queueType, *args):
        pass

    def onDequeued(self, queueType, *args):
        pass

    def onEnqueueError(self, queueType, *args):
        pass

    def onKickedFromQueue(self, queueType, *args):
        pass

    def onKickedFromArena(self, queueType, *args):
        pass

    def onArenaJoinFailure(self, queueType, *args):
        pass

    def onPreQueueSettingsChanged(self, diff):
        pass
