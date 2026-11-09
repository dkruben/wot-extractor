# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/random_national_bonus_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/random_national_bonus_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.random_national_bonus_tooltip_view_model import RandomNationalBonusTooltipViewModel
from gui.impl.pub import ViewImpl

class RandomNationalBonusTooltipView(ViewImpl):
    __slots__ = ('__name', '__value', '__icon')

    def __init__(self, name, value, icon):
        settings = ViewSettings(R.views.mono.lootbox.tooltips.random_national_bonus())
        settings.model = RandomNationalBonusTooltipViewModel()
        super(RandomNationalBonusTooltipView, self).__init__(settings)
        self.__name = name
        self.__value = value
        self.__icon = icon

    @property
    def viewModel(self):
        return super(RandomNationalBonusTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(RandomNationalBonusTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as vmTx:
            vmTx.setName(self.__name)
            vmTx.setValue(self.__value)
            vmTx.setIcon(self.__icon)
