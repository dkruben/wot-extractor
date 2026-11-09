# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/shared/clip/cassette_clip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/shared/clip/cassette_clip_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ClipState(Enum):
    NONE = 'none'
    NORMAL = 'normal'
    CRITICAL = 'critical'


class CassetteClipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CassetteClipModel, self).__init__(properties=properties, commands=commands)

    def getClipCapacity(self):
        return self._getNumber(0)

    def setClipCapacity(self, value):
        self._setNumber(0, value)

    def getBurst(self):
        return self._getNumber(1)

    def setBurst(self, value):
        self._setNumber(1, value)

    def getQuantityInClip(self):
        return self._getNumber(2)

    def setQuantityInClip(self, value):
        self._setNumber(2, value)

    def getClipState(self):
        return ClipState(self._getString(3))

    def setClipState(self, value):
        self._setString(3, value.value)

    def getClipReloaded(self):
        return self._getBool(4)

    def setClipReloaded(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(CassetteClipModel, self)._initialize()
        self._addNumberProperty('clipCapacity', -1)
        self._addNumberProperty('burst', -1)
        self._addNumberProperty('quantityInClip', -1)
        self._addStringProperty('clipState', ClipState.NONE.value)
        self._addBoolProperty('clipReloaded', False)
