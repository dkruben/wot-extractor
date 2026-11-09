# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush_dyn_object_cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush_dyn_object_cache.py
from __future__ import absolute_import
import typing, CGF
from dyn_objects_cache import DynObjectsBase

class _FortRushDynObjects(DynObjectsBase):

    def __init__(self):
        super(_FortRushDynObjects, self).__init__()
        self.__prefabPaths = []

    def init(self, dataSection):
        if self._initialized:
            return
        self.__prefabPaths = [value.asString for key, value in dataSection['prefabs'].items() if key == 'path' and value.asString]
        if self.__prefabPaths:
            CGF.cachePrefabs(self.__prefabPaths)
        super(_FortRushDynObjects, self).init(dataSection)

    def clear(self):
        if self.__prefabPaths:
            CGF.removePrefabsFromCache(list(self.__prefabPaths))
            del self.__prefabPaths[:]
        self._initialized = False
        super(_FortRushDynObjects, self).clear()

    def destroy(self):
        self.clear()
        super(_FortRushDynObjects, self).destroy()
