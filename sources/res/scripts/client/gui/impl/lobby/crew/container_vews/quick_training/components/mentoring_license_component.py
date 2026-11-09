# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/mentoring_license_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/mentoring_license_component.py
import typing
from gui.impl.gen import R
from gui.impl.lobby.container_views.base.components import ComponentBase
from gui.impl.lobby.crew.utils import getMetoringLicensesAmount
from gui.impl.lobby.crew.tooltips.mentoring_license_tooltip import MentoringLicenseTooltip
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.crew.quick_training.quick_training_view_model import QuickTrainingViewModel
    from gui.impl.gen.view_models.views.lobby.crew.quick_training.mentoring_license_component_model import MentoringLicenseComponentModel

class MentoringLicenseComponent(ComponentBase):

    def _getViewModel(self, vm):
        return vm.mentoringLicense

    def _getEvents(self):
        return super(MentoringLicenseComponent, self)._getEvents() + (
         (
          self.viewModel.openMentoring, self.events.onMentoringClick),)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.crew.tooltips.MentoringLicenseTooltip():
            return MentoringLicenseTooltip(getMetoringLicensesAmount())

    def _fillViewModel(self, vm):
        amount = getMetoringLicensesAmount()
        vm.setAmount(amount)
        vm.setIsEnabled(amount > 0 and not self.context.isAllCrewMaxTrained)
        vm.setIsVisible(self.context.isMentoringLicenseEnabled)
