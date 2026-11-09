# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/windows/piggy_bank_reward_window_content_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/piggy_bank_reward_window_content_model.py
from gui.impl.gen.view_models.windows.reward_window_content_model import RewardWindowContentModel

class PiggyBankRewardWindowContentModel(RewardWindowContentModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=3):
        super(PiggyBankRewardWindowContentModel, self).__init__(properties=properties, commands=commands)

    def getShowDescription(self):
        return self._getBool(3)

    def setShowDescription(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(PiggyBankRewardWindowContentModel, self)._initialize()
        self._addBoolProperty('showDescription', False)
