# wot-extractor: codigo DESCOMPILADO de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/modification_cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/modification_cache.py
from __future__ import absolute_import
from collections import deque
from typing import Optional, Any

class ModificationCache(object):
    DEFAULT_LAYER_COUNT = 0
    __slots__ = ('_modifications', '_maxLayerCount', '_layerIdQueue')

    def __init__(self, layerCount=None):
        if layerCount is None:
            layerCount = self.DEFAULT_LAYER_COUNT
        self._modifications = {}
        self._maxLayerCount = layerCount
        self._layerIdQueue = deque()
        return

    def clear(self):
        self._modifications.clear()
        self._layerIdQueue.clear()

    def _addLayer(self, layerId, initValue=None):
        if len(self._layerIdQueue) == self._maxLayerCount:
            del self._modifications[self._layerIdQueue.popleft()]
        self._layerIdQueue.append(layerId)
        self._modifications[layerId] = initValue
