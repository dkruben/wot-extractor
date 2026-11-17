# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/vehicle_compare_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel
from gui.impl.gen.view_models.views.lobby.page.footer.vehicle_compare_model import VehicleCompareModel as VehicleCompareModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache

# base nao representavel no stub: ViewComponent[...]
class VehicleComparePresenter:
    __itemsCache: Any
    __comparisonBasket: Any
    def __init__(self):
        ...
    def _getEvents(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onCountChanged(self, _):
        ...
    def __updateIsEnabled(self):
        ...
    def __updateVehicles(self):
        ...
