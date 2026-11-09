# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/sub_systems/base_sub_system.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/prebattle_highlights/sub_systems/base_sub_system.py
from __future__ import absolute_import

class BasePbhSubSystem(object):

    def __init__(self, readyCallback):
        self._readyCallback = readyCallback

    def subscribe(self):
        raise NotImplementedError

    def unsubscribe(self):
        raise NotImplementedError

    def isReady(self):
        raise NotImplementedError

    def startFlow(self):
        raise NotImplementedError

    def stopFlow(self):
        raise NotImplementedError

    def clear(self):
        self._readyCallback = None
        return
