# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/learning_results_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/learning_results_component.py
import typing
from gui.impl.lobby.container_views.base.components import ComponentBase
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.crew.quick_training.quick_training_view_model import QuickTrainingViewModel
    from gui.impl.gen.view_models.views.lobby.crew.quick_training.learning_results_component_model import LearningResultsComponentModel

class LearningResultsComponent(ComponentBase):

    def _getViewModel(self, vm):
        return vm.learningResults

    def _getEvents(self):
        return super(LearningResultsComponent, self)._getEvents() + (
         (
          self.viewModel.learn, self.events.onLearn),
         (
          self.viewModel.cancel, self.events.onCancel))

    def _fillViewModel(self, vm):
        freeXP = self.context.getAcquiringFreeXpValue()
        personalXP, commonXP = self.context.selection.getAcquiringBooksXpValues()
        vm.setPersonalXpAmount(personalXP + freeXP)
        vm.setCrewXpAmount(commonXP)
