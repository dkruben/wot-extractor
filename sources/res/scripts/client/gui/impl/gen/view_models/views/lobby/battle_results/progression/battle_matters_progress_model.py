# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/battle_matters_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/battle_matters_progress_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_view_model import QuestViewModel

class BattleMattersProgressModel(ViewModel):
    __slots__ = ('onNavigate', )
    PATH = 'coui://gui/gameface/_dist/production/mono/plugins/post_battle/battle_matters/battle_matters.js'

    def __init__(self, properties=2, commands=1):
        super(BattleMattersProgressModel, self).__init__(properties=properties, commands=commands)

    def getNavigationEnabled(self):
        return self._getBool(0)

    def setNavigationEnabled(self, value):
        self._setBool(0, value)

    def getBattleMatters(self):
        return self._getArray(1)

    def setBattleMatters(self, value):
        self._setArray(1, value)

    @staticmethod
    def getBattleMattersType():
        return QuestViewModel

    def _initialize(self):
        super(BattleMattersProgressModel, self)._initialize()
        self._addBoolProperty('navigationEnabled', False)
        self._addArrayProperty('battleMatters', Array())
        self.onNavigate = self._addCommand('onNavigate')
