# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/selected_mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/selected_mission_model.py
from story_mode.gui.impl.gen.view_models.views.lobby.mission_model import MissionModel

class SelectedMissionModel(MissionModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(SelectedMissionModel, self).__init__(properties=properties, commands=commands)

    def getIsCountdownVisible(self):
        return self._getBool(5)

    def setIsCountdownVisible(self, value):
        self._setBool(5, value)

    def getSecondsCountdown(self):
        return self._getNumber(6)

    def setSecondsCountdown(self, value):
        self._setNumber(6, value)

    def getBattlesToUnlock(self):
        return self._getNumber(7)

    def setBattlesToUnlock(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(SelectedMissionModel, self)._initialize()
        self._addBoolProperty('isCountdownVisible', False)
        self._addNumberProperty('secondsCountdown', 0)
        self._addNumberProperty('battlesToUnlock', 0)
