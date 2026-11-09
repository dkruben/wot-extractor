# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/blueprints/blueprints_alliance_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import nations as nations
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_price import BlueprintPrice as BlueprintPrice
from gui.impl.gen.view_models.views.lobby.blueprints.blueprints_alliance_tooltip_view_model import BlueprintsAllianceTooltipViewModel as BlueprintsAllianceTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class BlueprintsAllianceTooltipView(ViewImpl):
    __itemsCache: Any
    __nation: Any
    __vehicleIntCD: Any
    __vehicleLevel: Any
    def __init__(self, nation, vehicleIntCD, vehicleLevel):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __setPriceOptions(self, arrayModel):
        ...
