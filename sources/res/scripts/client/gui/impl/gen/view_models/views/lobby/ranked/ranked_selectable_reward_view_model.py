# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/ranked/ranked_selectable_reward_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/ranked/ranked_selectable_reward_view_model.py
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_base_model import SelectableRewardBaseModel

class RankedSelectableRewardViewModel(SelectableRewardBaseModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RankedSelectableRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getRewardType(self):
        return self._getString(1)

    def setRewardType(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(RankedSelectableRewardViewModel, self)._initialize()
        self._addStringProperty('rewardType', '')
