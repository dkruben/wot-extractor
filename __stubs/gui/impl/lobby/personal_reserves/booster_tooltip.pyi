# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/booster_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from frameworks.wulf import ViewSettings as ViewSettings
from gui.goodies.goodie_items import ClanReservePresenter as ClanReservePresenter, getFullNameForBoosterIcon as getFullNameForBoosterIcon
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import fillBoosterModelWithData as fillBoosterModelWithData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_reserves.booster_tooltip_model import BoosterTooltipModel as BoosterTooltipModel
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getBoostersInGroup as getBoostersInGroup
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IBoostersController as IBoostersController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from typing import Union as Union, Any as Any
from gui.goodies import GoodiesCache as GoodiesCache
from gui.goodies.goodie_items import Booster as Booster
from gui.shared.tooltips.contexts import BoosterInfoContext as BoosterInfoContext, ClanReserveContext as ClanReserveContext
from gui.game_control.BoostersController import BoostersController as BoostersController
BOOSTER_CONTEXT_TYPE: _Any
BOOSTER_TYPE: _Any

class BoosterTooltip(ViewImpl):
    goodiesCache: _Any
    _boosters: _Any
    __slots__: tuple
    boosterID: _Any
    context: _Any
    def __init__(self, boosterID, context):
        ...
    @property
    def viewModel(self):
        ...
    def _loadExpirableBoosters(self, booster):
        ...
    def _loadBoosterDefaults(self, booster):
        ...
    def _onLoading(self):
        ...
    def loadBooster(self):
        ...
    def _getEvents(self):
        ...
    def onBoosterChangeNotify(self):
        ...
