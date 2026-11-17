# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/quick_training_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.quick_training.quick_training_view_model import QuickTrainingViewModel as QuickTrainingViewModel
from gui.impl.lobby.container_views.base.components import ContainerBase as ContainerBase
from gui.impl.lobby.crew.base_crew_view import BaseCrewWidgetView as BaseCrewWidgetView
from gui.impl.lobby.crew.container_vews.quick_training.components.freexp_book_component import FreeXpBookComponent as FreeXpBookComponent
from gui.impl.lobby.crew.container_vews.quick_training.components.books_list_component import BooksListComponent as BooksListComponent
from gui.impl.lobby.crew.container_vews.quick_training.components.learning_results_component import LearningResultsComponent as LearningResultsComponent
from gui.impl.lobby.crew.container_vews.quick_training.components.mentoring_license_component import MentoringLicenseComponent as MentoringLicenseComponent
from gui.impl.lobby.crew.container_vews.quick_training.components.tips_list_component import TipsListComponent as TipsListComponent
from gui.impl.lobby.crew.container_vews.quick_training.context import QuickTrainingViewContext as QuickTrainingViewContext
from gui.impl.lobby.crew.container_vews.quick_training.controller import QuickTrainingInteractionController as QuickTrainingInteractionController
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.widget.crew_widget import QuickTrainingCrewWidget as QuickTrainingCrewWidget
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from typing import List as List, Type as Type
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController

class QuickTrainingView(ContainerBase, BaseCrewWidgetView):
    def __init__(self, layoutID=..., **kwargs):
        ...
    def _getComponents(self):
        ...
    def _getContext(self, *args, **kwargs):
        ...
    def _getInteractionControllerCls(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _fillViewModel(self, vm):
        ...
    @property
    def viewModel(self):
        ...
    def onBringToFront(self, parentWindow):
        ...
    def _getCrewWidgetBaseData(self):
        ...
    def _onTankmanSlotClick(self, tankmanID, slotIdx):
        ...
    def _onEmptySlotClick(self, tankmanID, slotIdx):
        ...
    def _onTankmanSlotAutoSelect(self, tankmanID, slotIdx):
        ...
    def _onInventoryChange(self, invDiff):
        ...
    def _onGoodiesUpdate(self, diff):
        ...
    def _onFreeXpChange(self, *_):
        ...
    def _onAbout(self):
        ...
    def _onCardMouseLeave(self):
        ...
    def _goToProfile(self):
        ...
    def setSelectedTman(self, tankmanID, slotIdx):
        ...
