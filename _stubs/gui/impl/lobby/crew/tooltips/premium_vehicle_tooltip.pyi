# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/premium_vehicle_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from frameworks.wulf import ViewSettings as ViewSettings
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.crew.tooltips.premium_vehicle_tooltip_view_model import PremiumVehicleTooltipViewModel as PremiumVehicleTooltipViewModel

class PremiumVehicleTooltip(ViewImpl):
    __slots__: tuple
    _itemsCache: Any
    __vehType: Any
    __nation: Any
    def __init__(self, vehicleCD, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
