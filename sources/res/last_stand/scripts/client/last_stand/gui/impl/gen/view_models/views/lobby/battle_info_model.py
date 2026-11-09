# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/battle_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/battle_info_model.py
from frameworks.wulf import ViewModel

class BattleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleInfoModel, self).__init__(properties=properties, commands=commands)

    def getMapName(self):
        return self._getString(0)

    def setMapName(self, value):
        self._setString(0, value)

    def getStartDate(self):
        return self._getString(1)

    def setStartDate(self, value):
        self._setString(1, value)

    def getDuration(self):
        return self._getString(2)

    def setDuration(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(BattleInfoModel, self)._initialize()
        self._addStringProperty('mapName', '')
        self._addStringProperty('startDate', '')
        self._addStringProperty('duration', '')
