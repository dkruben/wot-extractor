# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/battle_result_stat_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/battle_result_stat_tooltip_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.detailed_stat_model import DetailedStatModel

class StatEnum(Enum):
    MISSIONS = 'missions'
    ASSIST = 'assist'
    KILLS = 'kills'
    DAMAGE = 'damage'
    ARMOR_USE = 'armorUse'


class BattleResultStatTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleResultStatTooltipModel, self).__init__(properties=properties, commands=commands)

    def getStat(self):
        return StatEnum(self._getString(0))

    def setStat(self, value):
        self._setString(0, value.value)

    def getDetailedStats(self):
        return self._getArray(1)

    def setDetailedStats(self, value):
        self._setArray(1, value)

    @staticmethod
    def getDetailedStatsType():
        return DetailedStatModel

    def getInfoList(self):
        return self._getArray(2)

    def setInfoList(self, value):
        self._setArray(2, value)

    @staticmethod
    def getInfoListType():
        return unicode

    def _initialize(self):
        super(BattleResultStatTooltipModel, self)._initialize()
        self._addStringProperty('stat')
        self._addArrayProperty('detailedStats', Array())
        self._addArrayProperty('infoList', Array())
