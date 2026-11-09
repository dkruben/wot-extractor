# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_selection_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_selection_view_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_view_model import RewardViewModel

class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'


class RewardSelectionViewModel(ViewModel):
    __slots__ = ('onClose', 'onClaim')

    def __init__(self, properties=3, commands=2):
        super(RewardSelectionViewModel, self).__init__(properties=properties, commands=commands)

    def getMaxCertificates(self):
        return self._getNumber(0)

    def setMaxCertificates(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return RewardViewModel

    def getGender(self):
        return GenderEnum(self._getString(2))

    def setGender(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(RewardSelectionViewModel, self)._initialize()
        self._addNumberProperty('maxCertificates', 0)
        self._addArrayProperty('rewards', Array())
        self._addStringProperty('gender')
        self.onClose = self._addCommand('onClose')
        self.onClaim = self._addCommand('onClaim')
