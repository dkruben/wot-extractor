# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/conversion_confirm_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/conversion_confirm_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel

class ConversionConfirmViewModel(ViewModel):
    __slots__ = ('onConfirm', 'onShowTankman', 'onClose', 'onCancel')

    def __init__(self, properties=2, commands=4):
        super(ConversionConfirmViewModel, self).__init__(properties=properties, commands=commands)

    def getTankmanAmount(self):
        return self._getNumber(0)

    def setTankmanAmount(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def _initialize(self):
        super(ConversionConfirmViewModel, self)._initialize()
        self._addNumberProperty('tankmanAmount', 0)
        self._addArrayProperty('rewards', Array())
        self.onConfirm = self._addCommand('onConfirm')
        self.onShowTankman = self._addCommand('onShowTankman')
        self.onClose = self._addCommand('onClose')
        self.onCancel = self._addCommand('onCancel')
