# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSObeliskInfoComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSObeliskInfoComponent.py
from __future__ import absolute_import
import BigWorld
from Event import Event
from helpers import isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent

class ObeliskInfoStates(object):
    SHOW = 'show'
    HIT = 'hit'
    DEATH = 'death'
    HIDE = 'hide'


class LSObeliskInfoComponent(DynamicScriptComponent):

    def __init__(self):
        super(LSObeliskInfoComponent, self).__init__()
        self.onStateChange = Event()
        self.onObeliskObserved = Event()

    def onDestroy(self):
        self.onStateChange.clear()
        super(LSObeliskInfoComponent, self).onDestroy()

    def set_isPresent(self, _):
        if self.isPresent:
            self.onStateChange(ObeliskInfoStates.SHOW)
        else:
            self.onStateChange(ObeliskInfoStates.HIDE)

    def set_observedObeliskCD(self, _):
        self.onObeliskObserved(self.observedObeliskCD)

    def onDamageReceived(self):
        if self.isPresent:
            self.onStateChange(ObeliskInfoStates.HIT)

    def onDeath(self):
        self.onStateChange(ObeliskInfoStates.DEATH)

    @staticmethod
    def getInstance():
        if not isPlayerAvatar():
            return
        else:
            player = BigWorld.player()
            if not player or not player.arena:
                return
            return getattr(player.arena.arenaInfo, 'LSObeliskInfoComponent', None)

    def _onAvatarReady(self):
        super(LSObeliskInfoComponent, self)._onAvatarReady()
        self.onObeliskObserved(self.observedObeliskCD)
