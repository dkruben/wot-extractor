# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/missions/challenge_mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/challenge_mission_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel
from gui.impl.gen.view_models.views.lobby.challenges.bonus_model import BonusModel

class ChallengeMissionModel(QuestModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(ChallengeMissionModel, self).__init__(properties=properties, commands=commands)

    def getBonuses(self):
        return self._getArray(11)

    def setBonuses(self, value):
        self._setArray(11, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(ChallengeMissionModel, self)._initialize()
        self._addArrayProperty('bonuses', Array())
