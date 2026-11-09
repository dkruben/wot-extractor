# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/price_cards_content/perks_reset_price_list.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.goodies import IGoodiesCache as IGoodiesCache
from gui.impl.auxiliary.tankman_operations import packSkillReset as packSkillReset
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_list_model import PriceListModel as PriceListModel
from gui.impl.lobby.crew.dialogs.price_cards_content.base_price_list import BasePriceList as BasePriceList
from gui.impl.lobby.crew.utils import convertMoneyToTuple as convertMoneyToTuple
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Currency as Currency, DynamicMoney as DynamicMoney
from helpers import dependency as dependency
from items.tankmen import TankmanDescr as TankmanDescr, MIN_XP_REUSE_FRACTION as MIN_XP_REUSE_FRACTION, MAX_XP_REUSE_FRACTION as MAX_XP_REUSE_FRACTION
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from constants import SwitchState as SwitchState
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getPerksResetGracePeriod as getPerksResetGracePeriod
from gui.shared.utils.requesters import ShopRequester as ShopRequester
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel as PriceCardModel

class PerksResetPriceList(BasePriceList):
    __slots__: tuple
    __goodiesCache: Any
    __lobbyContext: Any
    _selectedOptionIndex: Any
    _recertificationOptionIdx: Any
    _tankman: Any
    _selectedCardIndex: Any
    _priceData: Any
    def __init__(self, tankmanId):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def selectedPriceData(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def _priceListPacker(self):
        ...
    def _getPriceData(self, index):
        ...
    def _onCardClick(self, args):
        ...
    def _onPriceSelect(self, args):
        ...
    def _getCallbacks(self):
        ...
    def _onGoodiesUpdate(self, *_):
        ...
    def _fillPrices(self):
        ...
    def _onTankmanChanged(self, data):
        ...
    def __getOperationData(self, cost):
        ...
