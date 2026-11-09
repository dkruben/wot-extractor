# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/prestige_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/prestige_view_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.rewards_slot_model import RewardsSlotModel

class PrestigeState(Enum):
    AVAILABLE = 'available'
    COMPLETED = 'completed'
    DISABLED = 'disabled'


class PrestigeViewModel(ViewModel):
    __slots__ = ('onPreview', )

    def __init__(self, properties=3, commands=1):
        super(PrestigeViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def prestigeEmblem(self):
        return self._getViewModel(0)

    @staticmethod
    def getPrestigeEmblemType():
        return PrestigeEmblemModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return RewardsSlotModel

    def getPrestigeState(self):
        return PrestigeState(self._getString(2))

    def setPrestigeState(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(PrestigeViewModel, self)._initialize()
        self._addViewModelProperty('prestigeEmblem', PrestigeEmblemModel())
        self._addArrayProperty('rewards', Array())
        self._addStringProperty('prestigeState')
        self.onPreview = self._addCommand('onPreview')
