# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/progression_screen/tiers_section_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/progression_screen/tiers_section_model.py
from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_reward_model import FrontlineRewardModel

class TiersSectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TiersSectionModel, self).__init__(properties=properties, commands=commands)

    def getStart(self):
        return self._getNumber(0)

    def setStart(self, value):
        self._setNumber(0, value)

    def getEnd(self):
        return self._getNumber(1)

    def setEnd(self, value):
        self._setNumber(1, value)

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)

    @staticmethod
    def getRewardsType():
        return FrontlineRewardModel

    def _initialize(self):
        super(TiersSectionModel, self)._initialize()
        self._addNumberProperty('start', 0)
        self._addNumberProperty('end', 0)
        self._addArrayProperty('rewards', Array())
