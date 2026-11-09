# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/battle_results/fun_random_battle_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/battle_results/fun_random_battle_info_model.py
from gui.impl.gen.view_models.views.lobby.battle_results.battle_info_model import BattleInfoModel

class FunRandomBattleInfoModel(BattleInfoModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(FunRandomBattleInfoModel, self).__init__(properties=properties, commands=commands)

    def getAssetsPointer(self):
        return self._getString(7)

    def setAssetsPointer(self, value):
        self._setString(7, value)

    def getSubModeAssetsPointer(self):
        return self._getString(8)

    def setSubModeAssetsPointer(self, value):
        self._setString(8, value)

    def getBattleType(self):
        return self._getString(9)

    def setBattleType(self, value):
        self._setString(9, value)

    def _initialize(self):
        super(FunRandomBattleInfoModel, self)._initialize()
        self._addStringProperty('assetsPointer', 'undefined')
        self._addStringProperty('subModeAssetsPointer', 'undefined')
        self._addStringProperty('battleType', 'standard')
