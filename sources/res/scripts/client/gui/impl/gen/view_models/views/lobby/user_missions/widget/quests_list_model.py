# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/quests_list_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/quests_list_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel

class QuestsListModel(ViewModel):
    __slots__ = ('onMissionClick', 'onMarkAsViewed')

    def __init__(self, properties=1, commands=2):
        super(QuestsListModel, self).__init__(properties=properties, commands=commands)

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)

    @staticmethod
    def getQuestsType():
        return WidgetQuestModel

    def _initialize(self):
        super(QuestsListModel, self)._initialize()
        self._addArrayProperty('quests', Array())
        self.onMissionClick = self._addCommand('onMissionClick')
        self.onMarkAsViewed = self._addCommand('onMarkAsViewed')
