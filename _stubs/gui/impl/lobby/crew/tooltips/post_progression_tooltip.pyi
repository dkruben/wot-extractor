# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/post_progression_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.post_progression_tooltip_model import PostProgressionTooltipModel as PostProgressionTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache

class PostProgressionTooltip(ViewImpl):
    __slots__: tuple
    _itemsCache: Any
    _tankmanID: Any
    def __init__(self, tankmanID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
