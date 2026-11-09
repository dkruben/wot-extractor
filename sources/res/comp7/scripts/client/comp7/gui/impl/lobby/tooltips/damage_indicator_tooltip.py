# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/damage_indicator_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/damage_indicator_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.damage_indicator_tooltip_model import DamageIndicatorTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class DamageIndicatorTooltip(ViewImpl):
    __slots__ = ('__params', )

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.damage_indicator_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = DamageIndicatorTooltipModel()
        super(DamageIndicatorTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(DamageIndicatorTooltip, self).getViewModel()

    def _onLoading(self):
        super(DamageIndicatorTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setStatisticsMode(self.__params['statisticsMode'])
            vm.setAverageDamageDealt(self.__params['averageDamageDealt'])
            vm.setRecordDamageDealt(self.__params['recordDamageDealt'])
            vm.setRecordDamageDealtVehicleName(self.__params['recordDamageDealtVehicleName'])
