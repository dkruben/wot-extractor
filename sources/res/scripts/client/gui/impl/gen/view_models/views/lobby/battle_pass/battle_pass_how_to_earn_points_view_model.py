# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_how_to_earn_points_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_how_to_earn_points_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_model import GameModeModel

class BattlePassHowToEarnPointsViewModel(ViewModel):
    __slots__ = ('onGoToMissions', 'onWotPlusClick')

    def __init__(self, properties=3, commands=2):
        super(BattlePassHowToEarnPointsViewModel, self).__init__(properties=properties, commands=commands)

    def getChapterID(self):
        return self._getNumber(0)

    def setChapterID(self, value):
        self._setNumber(0, value)

    def getGameModes(self):
        return self._getArray(1)

    def setGameModes(self, value):
        self._setArray(1, value)

    @staticmethod
    def getGameModesType():
        return GameModeModel

    def getIsWotPlusShown(self):
        return self._getBool(2)

    def setIsWotPlusShown(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(BattlePassHowToEarnPointsViewModel, self)._initialize()
        self._addNumberProperty('chapterID', 0)
        self._addArrayProperty('gameModes', Array())
        self._addBoolProperty('isWotPlusShown', False)
        self.onGoToMissions = self._addCommand('onGoToMissions')
        self.onWotPlusClick = self._addCommand('onWotPlusClick')
