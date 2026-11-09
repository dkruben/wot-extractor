# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/quick_training_discount_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/quick_training_discount_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.quick_training_discount_tooltip_model import QuickTrainingDiscountTooltipModel
from gui.impl.pub import ViewImpl

class QuickTrainingDiscountTooltip(ViewImpl):
    __slots__ = ('_oldFreeXpBase', '_newFreeXpBase', '_oldXpExchange', '_newXpExchange')

    def __init__(self, oldXpExchange, newXpExchange, oldFreeXpBase=1, newFreeXpBase=1):
        self._oldFreeXpBase = oldFreeXpBase
        self._newFreeXpBase = newFreeXpBase
        self._oldXpExchange = oldXpExchange
        self._newXpExchange = newXpExchange
        settings = ViewSettings(R.views.lobby.crew.tooltips.QuickTrainingDiscountTooltip(), model=QuickTrainingDiscountTooltipModel())
        super(QuickTrainingDiscountTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(QuickTrainingDiscountTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as vm:
            vm.setOldFreeXpBaseValue(self._oldFreeXpBase)
            vm.setNewFreeXpBaseValue(self._newFreeXpBase)
            vm.setOldXpExchangeValue(self._oldXpExchange)
            vm.setNewXpExchangeValue(self._newXpExchange)
