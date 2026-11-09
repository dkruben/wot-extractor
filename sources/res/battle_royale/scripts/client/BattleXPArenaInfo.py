# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/BattleXPArenaInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/BattleXPArenaInfo.py
from __future__ import absolute_import
import BigWorld

class BattleXPArenaInfo(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(BattleXPArenaInfo, self).__init__()
        self.__setAverageLevel()

    def set_vehiclesAverageBattleLevel(self, _):
        self.__setAverageLevel()

    def __setAverageLevel(self):
        progressionCtrl = self.entity.sessionProvider.dynamic.progression
        if progressionCtrl is not None:
            progressionCtrl.setAverageBattleLevel(self.vehiclesAverageBattleLevel)
        return
