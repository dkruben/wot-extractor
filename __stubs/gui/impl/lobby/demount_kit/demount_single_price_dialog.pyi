# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/demount_kit/demount_single_price_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.goodies.demount_kit import getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.goodies.goodie_items import DemountKit as DemountKit
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, CheckMoneyButton as CheckMoneyButton
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.footer.single_price_footer import SinglePriceFooter as SinglePriceFooter
from gui.impl.dialogs.sub_views.icon.item_icon import ItemIcons as ItemIcons
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencySize as CurrencySize, CurrencyType as CurrencyType
from gui.impl.gen.view_models.views.dialogs.template_settings.default_dialog_template_settings import DisplayFlags as DisplayFlags
from gui.impl.lobby.demount_kit.demount_kit_utils import getDemountDialogTitle as getDemountDialogTitle
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.money import Currency as Currency
from gui.shop import showBuyGoldForEquipment as showBuyGoldForEquipment
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice

class DemountOptionalDeviceSinglePriceDialog(DialogTemplateView):
    __slots__: tuple
    _itemsCache: Any
    __forFitting: Any
    __item: Any
    __dkAppeared: Any
    def __init__(self, itemCD, forFitting=False, layoutID=None, uniqueID=None):
        ...
    @property
    def itemPrice(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _inventorySyncHandler(self, *_):
        ...
    def _getAdditionalData(self):
        ...
    def _setResult(self, result):
        ...
