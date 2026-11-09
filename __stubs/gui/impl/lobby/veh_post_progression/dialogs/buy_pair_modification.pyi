# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/dialogs/buy_pair_modification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.fitting_types import FittingTypes as FittingTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.ammunition_buy_model import AmmunitionBuyModel as AmmunitionBuyModel
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_helpers import ConfirmedItemWarningTypes as ConfirmedItemWarningTypes
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.lobby.dialogs.contents.multiple_items_content import MultipleItemsContent as MultipleItemsContent
from gui.impl.lobby.tank_setup.dialogs.bottom_content.bottom_contents import PriceBottomContent as PriceBottomContent
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.veh_post_progression.models.ext_money import EXT_MONEY_ZERO as EXT_MONEY_ZERO
from post_progression_common import ACTION_TYPES as ACTION_TYPES
_logger: Any
ACTION_TYPE_TO_FITTING_TYPE: dict

# base nao representavel no stub: BuyAndExchange[...]
class BuyPairModificationDialog:
    _buyContent: Any
    _mainContent: Any
    __vehicle: Any
    __toStepID: Any
    __price: Any
    __modID: Any
    __item: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onInventoryResync(self, reason, diff):
        ...
    def __updateData(self):
        ...

class BuyPairModificationMainContent(MultipleItemsContent):
    __slots__: tuple
    _warnings: Any
    def __init__(self, viewModel, items, vehicleInvID=None, itemsType=None):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def _fillItems(self, array):
        ...
