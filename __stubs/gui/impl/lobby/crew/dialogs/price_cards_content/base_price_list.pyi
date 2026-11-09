# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/price_cards_content/base_price_list.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.auxiliary.tankman_operations import packPriceList as packPriceList
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel as PriceCardModel, CardState as CardState
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_list_model import PriceListModel as PriceListModel
from gui.impl.lobby.crew.utils import convertMoneyToTuple as convertMoneyToTuple
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from helpers_common import getRetrainCost as getRetrainCost, isAllRetrainOperationFree as isAllRetrainOperationFree
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import Array as Array
from skeletons.gui.shared.utils.requesters import IShopRequester as IShopRequester
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
GOLD_OPERATION = 2

class BasePriceList(ViewImpl):
    __slots__: tuple
    _itemsCache: Any
    _retrainCost: Any
    _selectedCardIndex: Any
    _priceData: Any
    onPriceChange: Any
    def __init__(self, settings):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def selectedPriceData(self):
        ...
    @property
    def selectedOperationData(self):
        ...
    def getOperationUselessInfo(self, tankman, targetRole, vehicle, cost, retrainCost, isMassRetrain=False):
        ...
    @property
    def _priceListPacker(self):
        ...
    def _deselectCurrentCard(self, vm):
        ...
    def _selectCard(self, vm, index=None):
        ...
    def _fillPrices(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @staticmethod
    def _getCard(vm, index):
        ...
    def _getPriceData(self, index):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _onTankmanChanged(self, data):
        ...
    def _onConsumeWalletUpdate(self, *_):
        ...
    def _onCreditsUpdate(self, *_):
        ...
    def _onGoldUpdate(self, *_):
        ...
    def _onCacheResync(self, reason, _):
        ...
    def _onCardClick(self, args):
        ...
    def _onPriceSelect(self, args):
        ...
    def __getMaxTmanSkillEfficiencyForEachOperation(self, cost, tankman, isRoleChanging, isOperationDisable, isMassRetrain):
        ...
