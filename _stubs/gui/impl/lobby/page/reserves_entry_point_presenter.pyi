# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/reserves_entry_point_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from goodies.goodie_constants import BoosterCategory as BoosterCategory
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import addToReserveArrayByCategory as addToReserveArrayByCategory
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel as BoosterModel
from gui.impl.gen.view_models.views.lobby.personal_reserves.reserves_entry_point_model import ReservesEntryPointModel as ReservesEntryPointModel
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getActiveBoosters as getActiveBoosters, addDisabledCategories as addDisabledCategories, getTotalReadyReserves as getTotalReadyReserves, getTotalLimitedReserves as getTotalLimitedReserves, getNearestExpiryTimeForToday as getNearestExpiryTimeForToday
from gui.impl.lobby.personal_reserves.tooltips.personal_reserves_tooltip_view import PersonalReservesTooltipView as PersonalReservesTooltipView
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.event_dispatcher import showBoostersActivation as showBoostersActivation
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IBoostersController as IBoostersController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.web import IWebController as IWebController
from frameworks.wulf.view.array import Array as Array
from frameworks.wulf.view.view import View as View, ViewEvent as ViewEvent
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class ReservesEntryPointPresenter:
    __boosters: Any
    __goodiesCache: Any
    __webCtrl: Any
    _hasActiveBoosters: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __updateClanReserves(self):
        ...
    def __updateModel(self):
        ...
    def __openBoosterNavigation(self):
        ...
