# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/mentoring_license_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/mentoring_license_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.mentoring_license_tooltip_model import MentoringLicenseTooltipModel
from gui.impl.pub import ViewImpl

class MentoringLicenseTooltip(ViewImpl):
    __slots__ = ('__amount', )

    def __init__(self, amount):
        self.__amount = amount
        settings = ViewSettings(R.views.lobby.crew.tooltips.MentoringLicenseTooltip(), model=MentoringLicenseTooltipModel())
        super(MentoringLicenseTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(MentoringLicenseTooltip, self).getViewModel()

    def _onLoading(self):
        self.viewModel.setAmount(self.__amount)
