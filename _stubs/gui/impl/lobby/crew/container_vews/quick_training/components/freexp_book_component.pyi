# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/freexp_book_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen import R as R
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.tooltips.experience_stepper_tooltip import ExperienceStepperTooltip as ExperienceStepperTooltip
from gui.impl.lobby.crew.tooltips.quick_training_discount_tooltip import QuickTrainingDiscountTooltip as QuickTrainingDiscountTooltip
from gui.impl.lobby.crew.utils import jsonArgsConverter as jsonArgsConverter
from gui.impl.gen.view_models.views.lobby.crew.quick_training.quick_training_view_model import QuickTrainingViewModel as QuickTrainingViewModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.freeXp_book_component_model import FreeXpBookComponentModel as FreeXpBookComponentModel

class FreeXpBookComponent(ComponentBase):
    def createToolTipContent(self, event, contentID):
        ...
    def _getViewModel(self, vm):
        ...
    def _getEvents(self):
        ...
    # decorador original: @jsonArgsConverter(...)
    def _onSelected(self, isSelected):
        ...
    # decorador original: @jsonArgsConverter(...)
    def _onManualInput(self, value):
        ...
    def _fillViewModel(self, vm):
        ...
