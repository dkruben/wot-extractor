# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/division_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/tooltips/division_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.division_tooltip_model import DivisionTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class DivisionTooltip(ViewImpl):
    __slots__ = ('__params', )

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.division_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = DivisionTooltipModel()
        super(DivisionTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(DivisionTooltip, self).getViewModel()

    def _onLoading(self):
        super(DivisionTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setRank(self.__params['rank'])
            vm.setDivision(self.__params['division'])
            vm.setFrom(self.__params['from'])
            vm.setTo(self.__params['to'])
