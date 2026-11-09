# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/challenge_missions/challenges_pack.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/challenge_missions/challenges_pack.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.challenge_missions.challenge_quest_model import ChallengeQuestModel

class ChallengesPack(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ChallengesPack, self).__init__(properties=properties, commands=commands)

    def getComplexity(self):
        return self._getString(0)

    def setComplexity(self, value):
        self._setString(0, value)

    def getChallenges(self):
        return self._getArray(1)

    def setChallenges(self, value):
        self._setArray(1, value)

    @staticmethod
    def getChallengesType():
        return ChallengeQuestModel

    def _initialize(self):
        super(ChallengesPack, self)._initialize()
        self._addStringProperty('complexity', '')
        self._addArrayProperty('challenges', Array())
