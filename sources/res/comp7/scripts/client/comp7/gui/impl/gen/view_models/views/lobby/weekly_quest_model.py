# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/weekly_quest_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/weekly_quest_model.py
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel

class WeeklyQuestModel(WidgetQuestModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(WeeklyQuestModel, self).__init__(properties=properties, commands=commands)

    def getQuestNumber(self):
        return self._getNumber(15)

    def setQuestNumber(self, value):
        self._setNumber(15, value)

    def _initialize(self):
        super(WeeklyQuestModel, self)._initialize()
        self._addNumberProperty('questNumber', 0)
