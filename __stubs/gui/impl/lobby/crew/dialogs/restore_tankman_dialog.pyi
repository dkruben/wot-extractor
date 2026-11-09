# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/restore_tankman_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.customization.shared import getPurchaseGoldForCredits as getPurchaseGoldForCredits, getPurchaseMoneyState as getPurchaseMoneyState, MoneyForPurchase as MoneyForPurchase
from gui.game_control.restore_contoller import getTankmenRestoreInfo as getTankmenRestoreInfo
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.dialogs.sub_views.footer.simple_text_footer import SimpleTextFooter as SimpleTextFooter
from gui.impl.dialogs.sub_views.footer.single_price_footer import SinglePriceFooter as SinglePriceFooter
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.lobby.crew.dialogs.restore_tankman_dialog_model import RestoreTankmanDialogModel as RestoreTankmanDialogModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel as setTankmanModel, setTmanSkillsModel as setTmanSkillsModel
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Tankman import Tankman as Tankman, NO_SLOT as NO_SLOT
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED
from helpers import dependency as dependency
from skeletons.gui.game_control import IRestoreController as IRestoreController
from skeletons.gui.shared import IItemsCache as IItemsCache

class RestoreTankmanDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = RestoreTankmanDialogModel
    _itemsCache: Any
    _restoreCtrl: Any
    _tankman: Any
    _vehicle: Any
    _vehicleSlotIdx: Any
    def __init__(self, tankmanId, vehicleId, slotIdx, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def restoreInfo(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setResult(self, result):
        ...
    def _restoreTankman(self):
        ...
    def __restoreTankman(self):
        ...
    def __onTankmenBufferUpdated(self):
        ...
    def __moneyChangeHandler(self, *_):
        ...
