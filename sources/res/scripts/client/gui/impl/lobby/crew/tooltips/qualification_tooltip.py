# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/qualification_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/tooltips/qualification_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.qualification_tooltip_view_model import QualificationTooltipViewModel
from gui.impl.pub import ViewImpl

class QualificationTooltip(ViewImpl):
    __slots__ = ('_qualificationIndex', '_roleName', '_isBonusQualification', '_isFemale')

    def __init__(self, qualificationIndex, roleName, isBonusQualification, isFemale):
        self._roleName = roleName
        self._isFemale = isFemale
        self._qualificationIndex = qualificationIndex
        self._isBonusQualification = isBonusQualification
        settings = ViewSettings(R.views.lobby.crew.tooltips.QualificationTooltip(), model=QualificationTooltipViewModel())
        super(QualificationTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(QualificationTooltip, self).getViewModel()

    def _onLoading(self):
        with self.viewModel.transaction() as vm:
            vm.setRoleName(self._roleName)
            vm.setIsFemale(self._isFemale)
            vm.setQualificationIndex(self._qualificationIndex + 1)
            vm.setIsBonusQualification(self._isBonusQualification)
