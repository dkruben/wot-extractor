# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/pre_battle_queue_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/pre_battle_queue_view_model.py
from last_stand.gui.impl.gen.view_models.views.lobby.vehicle_info_block_model import VehicleInfoBlockModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel
from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel

class PreBattleQueueViewModel(SelectableViewModel):
    __slots__ = ('onExitBattle', 'onEscape')

    def __init__(self, properties=4, commands=4):
        super(PreBattleQueueViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def selectedVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelectedVehicleType():
        return VehicleInfoBlockModel

    @property
    def selectedDifficulty(self):
        return self._getViewModel(1)

    @staticmethod
    def getSelectedDifficultyType():
        return DifficultyItemModel

    def getIsExitButtonAvailable(self):
        return self._getBool(2)

    def setIsExitButtonAvailable(self, value):
        self._setBool(2, value)

    def getTimerStartTime(self):
        return self._getNumber(3)

    def setTimerStartTime(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(PreBattleQueueViewModel, self)._initialize()
        self._addViewModelProperty('selectedVehicle', VehicleInfoBlockModel())
        self._addViewModelProperty('selectedDifficulty', DifficultyItemModel())
        self._addBoolProperty('isExitButtonAvailable', False)
        self._addNumberProperty('timerStartTime', 0)
        self.onExitBattle = self._addCommand('onExitBattle')
        self.onEscape = self._addCommand('onEscape')
