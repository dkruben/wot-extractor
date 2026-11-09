# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/filters/filter_by_nation.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import nations as nations
from gui import GUI_NATIONS as GUI_NATIONS
from gui.Scaleform.daapi.view.meta.ItemsWithTypeAndNationFilterTabViewMeta import ItemsWithTypeAndNationFilterTabViewMeta as ItemsWithTypeAndNationFilterTabViewMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA

class FiltrableInventoryCategoryByNationTabView(ItemsWithTypeAndNationFilterTabViewMeta):
    __selectedNationID: Any
    def __init__(self):
        ...
    def selectNation(self, id):
        ...
    def resetFilter(self):
        ...
    def _parseLoadedFilters(self, filterDict):
        ...
    def _prepareDataForFilterSaving(self):
        ...
    def _initFilter(self):
        ...
    def _shouldShowCounter(self):
        ...
    def _getFilteredCriteria(self):
        ...
