# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/oit_availability_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/oit_availability_controller.py
from __future__ import absolute_import
import BigWorld
from PlayerEvents import g_playerEvents
from config_schemas.oit_availability import oitAvailabilitySchema
from skeletons.gui.game_control import IOitAvailabilityController

class OitAvailabilityController(IOitAvailabilityController):

    def init(self):
        g_playerEvents.onConfigModelUpdated += self._onConfigModelUpdated

    def fini(self):
        g_playerEvents.onConfigModelUpdated -= self._onConfigModelUpdated

    def onAccountBecomePlayer(self):
        self._pushToEngine()

    def onAvatarBecomePlayer(self):
        self._pushToEngine()

    def isOitEnabledForPreset(self, qualityLevel):
        return BigWorld.isOitEnabledForPreset(qualityLevel)

    def _onConfigModelUpdated(self, gpKey):
        if oitAvailabilitySchema.gpKey == gpKey:
            self._pushToEngine()

    def _pushToEngine(self):
        config = oitAvailabilitySchema.getModel()
        if config is not None:
            BigWorld.configureOitPresets(config.min, config.low, config.medium, config.high, config.ultra)
        return
