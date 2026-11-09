# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_royale_respawn_ability_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_royale_respawn_ability_model.py
from frameworks.wulf import ViewModel

class BattleRoyaleRespawnAbilityModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleRoyaleRespawnAbilityModel, self).__init__(properties=properties, commands=commands)

    def getSoloRespawnPeriod(self):
        return self._getNumber(0)

    def setSoloRespawnPeriod(self, value):
        self._setNumber(0, value)

    def getPlatoonRespawnPeriod(self):
        return self._getNumber(1)

    def setPlatoonRespawnPeriod(self, value):
        self._setNumber(1, value)

    def getPlatoonTimeToResurrect(self):
        return self._getNumber(2)

    def setPlatoonTimeToResurrect(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(BattleRoyaleRespawnAbilityModel, self)._initialize()
        self._addNumberProperty('soloRespawnPeriod', 0)
        self._addNumberProperty('platoonRespawnPeriod', 0)
        self._addNumberProperty('platoonTimeToResurrect', 0)
