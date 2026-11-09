# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/ThunderStrike.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/ThunderStrike.py
from __future__ import absolute_import
import BigWorld
from Event import Event
from helpers.CallbackDelayer import CallbackDelayer
from debug_utils import LOG_DEBUG_DEV

class ThunderStrike(BigWorld.Entity, CallbackDelayer):

    def __init__(self):
        super(ThunderStrike, self).__init__()
        LOG_DEBUG_DEV('ArenaInfoThunderStrikeLauncher launched', self.position, self.equipmentID)
        self.onHit = Event()

    def hitThunderStrike(self):
        LOG_DEBUG_DEV('hitThunderStrike')
        self.onHit()
