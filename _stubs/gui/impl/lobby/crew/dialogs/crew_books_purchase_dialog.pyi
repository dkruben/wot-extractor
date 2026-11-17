# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/crew_books_purchase_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.customization.shared import getPurchaseGoldForCredits as getPurchaseGoldForCredits, getPurchaseMoneyState as getPurchaseMoneyState, MoneyForPurchase as MoneyForPurchase
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType as CurrencyType, CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.lobby.crew.dialogs.crew_books_purchase_dialog_model import CrewBooksPurchaseDialogModel as CrewBooksPurchaseDialogModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.processors.module import BookBuyer as BookBuyer
from gui.shared.tooltips.common import getSimpleTooltipFactory as getSimpleTooltipFactory
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
INITIAL_BOOK_COUNT = 1

class CrewBooksPurchaseDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = CrewBooksPurchaseDialogModel
    _itemsCache: Any
    _bookGuiItem: Any
    _bookCount: Any
    def __init__(self, crewBookCD):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def purchasePrice(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _addListener(self):
        ...
    def _removeListener(self):
        ...
    def _setTitle(self, book):
        ...
    def _getToolTipBuilder(self):
        ...
    # decorador original: @args2params(...)
    def _onStepperChanged(self, quantity):
        ...
    def __onMoneyUpdated(self, _):
        ...
    def _updateViewModel(self):
        ...
    def _updatePrice(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setBookPrice(self, vm):
        ...
    def _setResult(self, result):
        ...
    def _buyBook(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _executeBuy(self):
        ...
