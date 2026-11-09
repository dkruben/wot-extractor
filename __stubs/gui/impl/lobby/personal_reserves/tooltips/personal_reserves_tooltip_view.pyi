# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/tooltips/personal_reserves_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_reserves.reserves_entry_point_model import ReservesEntryPointModel as ReservesEntryPointModel
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getActiveBoosters as getActiveBoosters, getTotalReadyReserves as getTotalReadyReserves, getTotalLimitedReserves as getTotalLimitedReserves, addDisabledCategories as addDisabledCategories
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import addToReserveArrayByCategory as addToReserveArrayByCategory
from gui.impl.pub import ViewImpl as ViewImpl
from goodies.goodie_constants import BoosterCategory as BoosterCategory
from helpers import dependency as dependency
from skeletons.gui.game_control import IBoostersController as IBoostersController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.web import IWebController as IWebController
import Event as Event
from typing import Tuple as Tuple, Callable as Callable, Optional as Optional
from gui.wgcg.web_controller import WebController as WebController
from gui.goodies.goodies_cache import GoodiesCache as GoodiesCache
from gui.game_control.BoostersController import BoostersController as BoostersController

class PersonalReservesTooltipView(ViewImpl):
    _webCtrl: Any
    _goodiesCache: Any
    _boosters: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self):
        ...
    def _update(self):
        ...
    def _isInClan(self):
        ...
    def _canAddEmptySection(self, category):
        ...
