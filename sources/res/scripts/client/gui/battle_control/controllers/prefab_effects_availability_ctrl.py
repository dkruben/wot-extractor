# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/prefab_effects_availability_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/prefab_effects_availability_ctrl.py
from __future__ import absolute_import
import BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from config_schemas.prefab_effects_availability import prefabEffectsAvailabilitySchema
from gui.battle_control.arena_info.interfaces import IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from helpers.prefab_effects import setCachePrefabEffectsEnabledForBattle, resetCachePrefabEffectsEnabledForBattle

class PrefabEffectsAvailabilityController(IArenaLoadController):
    __slots__ = ()

    def startControl(self, battleCtx, arenaVisitor):
        from PlayerEvents import g_playerEvents
        g_playerEvents.onConfigModelUpdated += self._onConfigModelUpdated

    def stopControl(self):
        from PlayerEvents import g_playerEvents
        g_playerEvents.onConfigModelUpdated -= self._onConfigModelUpdated
        resetCachePrefabEffectsEnabledForBattle()

    def getControllerID(self):
        return BATTLE_CTRL_ID.PREFAB_EFFECTS_AVAILABILITY_CTRL

    def spaceLoadStarted(self):
        self._pushValue()

    def _onConfigModelUpdated(self, gpKey):
        if prefabEffectsAvailabilitySchema.gpKey == gpKey:
            self._pushValue()

    def _pushValue(self):
        config = prefabEffectsAvailabilitySchema.getModel()
        globalEnabled = config.enabled if config is not None else True
        enabledForBattle = globalEnabled and not BigWorld.player().hasBonusCap(_CAPS.NO_PREFAB_EFFECTS)
        setCachePrefabEffectsEnabledForBattle(enabledForBattle)
        return
