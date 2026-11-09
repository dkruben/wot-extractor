# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/reward_path_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/reward_path_view_model.py
from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.reward_path_artefact_view_model import RewardPathArtefactViewModel

class RewardPathViewModel(ViewModel):
    __slots__ = ('onClose', 'onViewLoaded', 'onAbout', 'onShowIntro', 'goToMission')

    def __init__(self, properties=4, commands=5):
        super(RewardPathViewModel, self).__init__(properties=properties, commands=commands)

    def getArtefacts(self):
        return self._getArray(0)

    def setArtefacts(self, value):
        self._setArray(0, value)

    @staticmethod
    def getArtefactsType():
        return RewardPathArtefactViewModel

    def getPoints(self):
        return self._getNumber(1)

    def setPoints(self, value):
        self._setNumber(1, value)

    def getCurrentArtefactID(self):
        return self._getString(2)

    def setCurrentArtefactID(self, value):
        self._setString(2, value)

    def getOpenFromQuestCard(self):
        return self._getBool(3)

    def setOpenFromQuestCard(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(RewardPathViewModel, self)._initialize()
        self._addArrayProperty('artefacts', Array())
        self._addNumberProperty('points', 0)
        self._addStringProperty('currentArtefactID', '')
        self._addBoolProperty('openFromQuestCard', False)
        self.onClose = self._addCommand('onClose')
        self.onViewLoaded = self._addCommand('onViewLoaded')
        self.onAbout = self._addCommand('onAbout')
        self.onShowIntro = self._addCommand('onShowIntro')
        self.goToMission = self._addCommand('goToMission')
