# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/excluded_maps/map_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/excluded_maps/map_item_model.py
from frameworks.wulf import ViewModel

class MapItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MapItemModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)

    def getCooldownEndTime(self):
        return self._getNumber(2)

    def setCooldownEndTime(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(MapItemModel, self)._initialize()
        self._addStringProperty('state', '')
        self._addStringProperty('mapId', '')
        self._addNumberProperty('cooldownEndTime', 0)
