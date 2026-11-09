# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/referral_program_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/referral_program_model.py
from frameworks.wulf import ViewModel

class ReferralProgramModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=4, commands=1):
        super(ReferralProgramModel, self).__init__(properties=properties, commands=commands)

    def getFirstIndication(self):
        return self._getBool(0)

    def setFirstIndication(self, value):
        self._setBool(0, value)

    def getNewReferralSeason(self):
        return self._getBool(1)

    def setNewReferralSeason(self, value):
        self._setBool(1, value)

    def getEnabled(self):
        return self._getBool(2)

    def setEnabled(self, value):
        self._setBool(2, value)

    def getBubbleCount(self):
        return self._getNumber(3)

    def setBubbleCount(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(ReferralProgramModel, self)._initialize()
        self._addBoolProperty('firstIndication', False)
        self._addBoolProperty('newReferralSeason', False)
        self._addBoolProperty('enabled', False)
        self._addNumberProperty('bubbleCount', 0)
        self.onClick = self._addCommand('onClick')
