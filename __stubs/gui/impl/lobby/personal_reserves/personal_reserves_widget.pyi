# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Event as Event
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from goodies.goodie_constants import BoosterCategory as BoosterCategory
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel as BoosterModel
from gui.impl.gen.view_models.views.lobby.personal_reserves.reserves_entry_point_model import ReservesEntryPointModel as ReservesEntryPointModel
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getActiveBoosters as getActiveBoosters, getTotalReadyReserves as getTotalReadyReserves, getTotalLimitedReserves as getTotalLimitedReserves, addDisabledCategories as addDisabledCategories, getNearestExpiryTimeForToday as getNearestExpiryTimeForToday
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import addToReserveArrayByCategory as addToReserveArrayByCategory
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IBoostersController as IBoostersController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from frameworks.wulf.view.array import Array as Array
from gui.shared.items_cache import ItemsCache as ItemsCache
from gui.goodies.goodies_cache import GoodiesCache as GoodiesCache
from gui.game_control.BoostersController import BoostersController as BoostersController
from gui.wgcg.web_controller import WebController as WebController
_logger: Any

class PersonalReservesWidget(ViewImpl):
    _boosters: Any
    _goodiesCache: Any
    _itemsCache: Any
    __webCtrl: Any
    _hasActiveBoosters: Any
    onUpdate: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def hasActiveBoosters(self):
        ...
    @property
    def activeBoostersCount(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self):
        ...
    def _fillViewModel(self, model):
        ...
    def _update(self):
        ...
    def _onClanInfoChanged(self, _):
        ...
    def _updateClanReserves(self):
        ...
