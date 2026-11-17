# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/ability_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.ability_tooltip_view_model import AbilityTooltipViewModel as AbilityTooltipViewModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class AbilityTooltipView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __showPriceBlock: Any
    item: Any
    def __init__(self, intCD, showPriceBlock=True):
        ...
    @property
    def viewModel(self):
        ...
    @staticmethod
    def _getInstalledVehicles(module, inventoryVehicles):
        ...
    def _onLoading(self):
        ...
