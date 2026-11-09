# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/confirm_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.fitting_types import FittingTypes as FittingTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.ammunition_buy_model import AmmunitionBuyModel as AmmunitionBuyModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.confirm_bottom_content_type import ConfirmBottomContentType as ConfirmBottomContentType
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContentResult as ExchangeContentResult
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.ammunition_buy_helper import isFreeInstalling as isFreeInstalling
from gui.impl.lobby.tank_setup.dialogs.main_content.main_contents import AmmunitionBuyMainContent as AmmunitionBuyMainContent
from gui.shared.money import ZERO_MONEY as ZERO_MONEY
from gui.impl.lobby.tank_setup.dialogs.bottom_content.bottom_contents import AmmunitionBuyBottomContent as AmmunitionBuyBottomContent
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
_logger: Any
_SECTION_TO_FITTING_TYPE: dict

class TankSetupConfirmDialog(BuyAndExchange):
    __slots__: tuple
    __items: Any
    __vehicleInvID: Any
    __totalPrice: Any
    _mainContent: Any
    _buyContent: Any
    _itemsType: Any
    __startState: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def items(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onInventoryResync(self, *args, **kwargs):
        ...
    def _transitToExchange(self):
        ...
    def _exchangeComplete(self, result):
        ...
    def _stateToContent(self):
        ...
    def _buyNotRequiredAccept(self):
        ...

class TankSetupExitConfirmDialog(TankSetupConfirmDialog):
    __slots__: tuple
    _itemsType: Any
    __rollBack: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getAdditionalData(self):
        ...
    def _onCancelClicked(self):
        ...
    def _onInventoryResync(self, *args, **kwargs):
        ...
    def __isNeedToCheckCount(self):
        ...
    def __isChangedInInventory(self):
        ...
