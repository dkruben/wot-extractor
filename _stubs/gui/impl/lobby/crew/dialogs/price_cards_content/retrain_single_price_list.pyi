# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/price_cards_content/retrain_single_price_list.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array
from gui.impl.auxiliary.tankman_operations import packSingleRetrain as packSingleRetrain
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel as PriceCardModel, CardState as CardState
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_list_model import PriceListModel as PriceListModel
from gui.impl.lobby.crew.dialogs.price_cards_content.base_price_list import BasePriceList as BasePriceList
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Currency as Currency, Money as Money
from helpers_common import getFinalRetrainCost as getFinalRetrainCost, isAllRetrainOperationFree as isAllRetrainOperationFree
from items.tankmen import TankmanDescr as TankmanDescr
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from skeletons.gui.shared.utils.requesters import IShopRequester as IShopRequester
_TOOLTIP_LOC = R.strings.tooltips.retrain.priceCard.disable

class RetrainSinglePriceList(BasePriceList):
    __slots__: tuple
    _tankman: Any
    _vehicle: Any
    _targetRole: Any
    _priceData: Any
    def __init__(self, tankmanId, vehicleCD, targetRole=None):
        ...
    @property
    def _priceListPacker(self):
        ...
    def _deselectCurrentCard(self, vm):
        ...
    @property
    def isRoleChangeAvailable(self):
        ...
    @property
    def selectedOperationData(self):
        ...
    @property
    def isAllRetrainOperationFree(self):
        ...
    def updateTargetRole(self, role):
        ...
    @staticmethod
    def _getDisableTooltipData(isDiscount, isUseless, isDisableByRoleChange):
        ...
    def _getOperationCustomData(self, tankman, cost):
        ...
    def _getOperationData(self, cost):
        ...
    def _fillPrices(self):
        ...
    def _onTankmanChanged(self, _):
        ...
