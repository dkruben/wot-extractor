# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/post_progression_widget_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.impl.gen import R as R
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.tooltips.post_progression_tooltip import PostProgressionTooltip as PostProgressionTooltip
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Any as Any, Callable as Callable, Tuple as Tuple
from gui.impl.gen.view_models.views.lobby.crew.personal_case.post_progression_widget_model import PostProgressionWidgetModel as PostProgressionWidgetModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_file_view_model import PersonalFileViewModel as PersonalFileViewModel

class PostProgressionWidgetComponent(ComponentBase):
    _itemsCache: _Any
    _appLoader: _Any
    def createToolTipContent(self, event, contentID):
        ...
    def _getViewModel(self, vm):
        ...
    def _getEvents(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setPostProgression(self, vm):
        ...
    def _onWidgetClick(self):
        ...
