# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/daily_quests_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/daily_quests_progress_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.daily_quest_progress_model import DailyQuestProgressModel

class DailyQuestsProgressModel(ViewModel):
    __slots__ = ('onNavigate', )
    PATH = 'coui://gui/gameface/_dist/production/mono/plugins/post_battle/daily_quests/daily_quests.js'

    def __init__(self, properties=1, commands=1):
        super(DailyQuestsProgressModel, self).__init__(properties=properties, commands=commands)

    def getDailyQuests(self):
        return self._getArray(0)

    def setDailyQuests(self, value):
        self._setArray(0, value)

    @staticmethod
    def getDailyQuestsType():
        return DailyQuestProgressModel

    def _initialize(self):
        super(DailyQuestsProgressModel, self)._initialize()
        self._addArrayProperty('dailyQuests', Array())
        self.onNavigate = self._addCommand('onNavigate')
