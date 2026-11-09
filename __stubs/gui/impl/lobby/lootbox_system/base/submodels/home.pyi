# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/submodels/home.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from account_helpers.AccountSettings import LOOT_BOXES_SELECTED_BOX as LOOT_BOXES_SELECTED_BOX
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from gui.impl.gen.view_models.views.lobby.lootbox_system.main_view_model import SubViewID as SubViewID
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.home_view_model import HomeViewModel as HomeViewModel
from gui.impl.lobby.lootbox_system.base.common import SubViewImpl as SubViewImpl
from gui.impl.lobby.lootbox_system.base.submodels.common import updateAnimationState as updateAnimationState, updateBoxesInfoModel as updateBoxesInfoModel
from gui.impl.lobby.lootbox_system.base.submodels.statistics import Statistics as Statistics
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.lootbox_system.base.decorators import createTooltipContentDecorator as createTooltipContentDecorator
from gui.lootbox_system.base.utils import getOpeningOptions as getOpeningOptions, getPreferredBox as getPreferredBox, openBoxes as openBoxes, isShopVisible as isShopVisible
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from typing import Dict as Dict, List as List
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_OPENING_OPTION_KEY = 'openingOption'

class Home(SubViewImpl):
    __lootBoxes: Any
    __options: dict
    _stats: Any
    __isResetCompleted: Any
    __isOpeningInProgress: Any
    __boxOption: Any
    __eventName: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def boxCategory(self):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateData(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateCounters(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateAnimationState(self, ctx=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateSelectedBoxOption(self, ctx=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateOpeningOptions(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateSelectedOpeningOption(self, ctx=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __resetSelectedOpeningOption(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __resetError(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateStatistics(self, model=None):
        ...
    def __getDefaultBoxOption(self):
        ...
    def __getBoxOptions(self):
        ...
    def __showInfo(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __openBoxes(self, ctx, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onErrorBack(self, _, model=None):
        ...
    def __buyBoxes(self):
        ...
    def __onUpdateResetState(self):
        ...
    def __onUpdateReset(self, event):
        ...
    def __onStatisticsReset(self):
        ...
    def __onStatusChanged(self):
        ...
    def __updateTime(self, model=None):
        ...
    def __getEventExpireTime(self):
        ...
