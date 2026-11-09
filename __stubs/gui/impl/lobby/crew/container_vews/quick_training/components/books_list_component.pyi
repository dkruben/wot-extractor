# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/books_list_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.quick_training.books_list_component_model import TrainingBookModel as TrainingBookModel
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.tooltips.crew_book_mouse_tooltip import CrewBookMouseTooltip as CrewBookMouseTooltip
from gui.impl.lobby.crew.tooltips.quick_training_lostxp_tooltip import QuickTrainingLostXpTooltip as QuickTrainingLostXpTooltip
from gui.impl.lobby.crew.utils import jsonArgsConverter as jsonArgsConverter
from typing import List as List
from gui.impl.gen.view_models.views.lobby.crew.quick_training.quick_training_view_model import QuickTrainingViewModel as QuickTrainingViewModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.books_list_component_model import BooksListComponentModel as BooksListComponentModel
from gui.shared.gui_items.crew_book import CrewBook as CrewBook

class BooksListComponent(ComponentBase):
    def createToolTipContent(self, event, contentID):
        ...
    def _getViewModel(self, vm):
        ...
    def _getEvents(self):
        ...
    # decorador original: @jsonArgsConverter(...)
    def _onBuyBook(self, bookId):
        ...
    # decorador original: @jsonArgsConverter(...)
    def _onBookMouseEnter(self, intCD):
        ...
    # decorador original: @jsonArgsConverter(...)
    def _onBookSelected(self, intCD, count):
        ...
    def _fillViewModel(self, vm):
        ...
    def __fillBookItemModel(self, book, rewardBook, hiddenItems, canUseBook, isDisabled, hasError, hasMaxedTankmen):
        ...
