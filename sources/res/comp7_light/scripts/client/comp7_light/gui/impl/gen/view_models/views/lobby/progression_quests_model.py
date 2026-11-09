# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/progression_quests_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/progression_quests_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel

class ProgressionQuestsModel(ViewModel):
    __slots__ = ('onMissionClick', 'onMarkAsViewed')

    def __init__(self, properties=2, commands=2):
        super(ProgressionQuestsModel, self).__init__(properties=properties, commands=commands)

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)

    @staticmethod
    def getQuestsType():
        return WidgetQuestModel

    def getIsMissionsEnable(self):
        return self._getBool(1)

    def setIsMissionsEnable(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(ProgressionQuestsModel, self)._initialize()
        self._addArrayProperty('quests', Array())
        self._addBoolProperty('isMissionsEnable', True)
        self.onMissionClick = self._addCommand('onMissionClick')
        self.onMarkAsViewed = self._addCommand('onMarkAsViewed')
