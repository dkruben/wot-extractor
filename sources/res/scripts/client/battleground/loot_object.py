# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/battleground/loot_object.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/battleground/loot_object.py
from __future__ import absolute_import
import logging, BigWorld, CGF
from helpers import dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(dynamicObjectsCache=IBattleDynamicObjectsCache, battleSession=IBattleSessionProvider)
def loadLootById(typeID, dynamicObjectsCache=None, battleSession=None):
    descr = dynamicObjectsCache.getConfig(battleSession.arenaVisitor.getArenaGuiType()).getLoots().get(typeID, None)
    if descr is None:
        _logger.error('[Loot] Could not find loot types for %s.', typeID)
    return descr


class SteelHunterDynamicObjectsCachingManager(CGF.System):
    __dynamicObjectsCache = dependency.descriptor(IBattleDynamicObjectsCache)

    def __init__(self):
        super(SteelHunterDynamicObjectsCachingManager, self).__init__()
        self.__cachedPrefabs = set()
        self.__cachedConfig = None
        return

    def activate(self):
        config = self.__getConfig()
        loots = config.getLoots().values()
        for loot in loots:
            self.__cachePrefabs(loot)

    def deactivate(self):
        if self.__cachedPrefabs:
            CGF.removePrefabsFromCache(list(self.__cachedPrefabs))

    def __cachePrefabs(self, lootDescr):
        if lootDescr is not None:
            for path in ('prefab', 'prefabPickup'):
                prefabPath = getattr(lootDescr, path, None)
                if prefabPath:
                    self.__cachedPrefabs.add(prefabPath)

        if self.__cachedPrefabs:
            CGF.cachePrefabs(list(self.__cachedPrefabs))
        return

    def __getConfig(self):
        if self.__cachedConfig is None:
            self.__cachedConfig = self.__dynamicObjectsCache.getConfig(BigWorld.player().arenaGuiType)
        return self.__cachedConfig
