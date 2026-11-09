# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/battle/tooltips/ban_show_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/battle/tooltips/ban_show_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.battle.tooltips.ban_show_tooltip_model import BanShowTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class BanShowTooltip(ViewImpl):
    __slots__ = ('__params', )

    def __init__(self, layoutID=R.views.comp7.mono.battle.tooltips.ban_show_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = BanShowTooltipModel()
        super(BanShowTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(BanShowTooltip, self).getViewModel()

    def _onLoading(self):
        super(BanShowTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setLongName(self.__params['longName'])
            vm.setType(self.__params['type'])
            vm.setIsPremium(self.__params['isPremium'])
            vm.setConfirmedChoice(self.__params['confirmedChoice'])
            vm.setVehicleCD(self.__params['vehicleCD'])
            vm.setRoleKey(self.__params['roleKey'])
