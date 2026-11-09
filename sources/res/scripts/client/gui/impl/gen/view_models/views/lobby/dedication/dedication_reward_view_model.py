# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dedication/dedication_reward_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dedication/dedication_reward_view_model.py
from frameworks.wulf import Array, ViewModel

class DedicationRewardViewModel(ViewModel):
    __slots__ = ()
    BATTLES_150K = '150'
    BATTLES_200K = '200'
    BATTLES_250K = '250'
    BATTLES_300K = '300'

    def __init__(self, properties=2, commands=0):
        super(DedicationRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)

    def getLevel(self):
        return self._getString(1)

    def setLevel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DedicationRewardViewModel, self)._initialize()
        self._addArrayProperty('mainRewards', Array())
        self._addStringProperty('level', '')
