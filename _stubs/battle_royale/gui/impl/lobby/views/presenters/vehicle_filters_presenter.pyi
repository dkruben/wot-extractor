# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/vehicle_filters_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import BigWorld as BigWorld
from account_helpers.settings_core import settings_constants as settings_constants
from battle_royale.gui.impl.gen.view_models.views.lobby.views.vehicles_filter_model import VehiclesFilterModel as VehiclesFilterModel
from gui import GUI_NATIONS as GUI_NATIONS
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from typing import Any as Any

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleVehicleFiltersPresenter:
    __settingsCore: _Any
    __rowCount: _Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __updateModel(self):
        ...
    def __onCarouselSettingsChange(self, diff):
        ...
    def __updateCarousel(self):
        ...
    def __readSettings(self):
        ...
