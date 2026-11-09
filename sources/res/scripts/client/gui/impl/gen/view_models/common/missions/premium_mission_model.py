# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/missions/premium_mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/premium_mission_model.py
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel

class PremiumMissionModel(QuestModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(PremiumMissionModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getString(11)

    def setIcon(self, value):
        self._setString(11, value)

    def _initialize(self):
        super(PremiumMissionModel, self)._initialize()
        self._addStringProperty('icon', '')
