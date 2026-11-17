# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/demount_kit/demount_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.goodies.demount_kit import getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.goodies.goodie_items import DemountKit as DemountKit
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.content.select_option_content import SelectOptionContent as SelectOptionContent, DemountKitOption as DemountKitOption, MoneyOption as MoneyOption
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.dialogs.template_settings.default_dialog_template_settings import DisplayFlags as DisplayFlags
from gui.impl.lobby.demount_kit.demount_kit_utils import getDemountDialogTitle as getDemountDialogTitle
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shop import showBuyGoldForEquipment as showBuyGoldForEquipment
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
NOTHING = -1
DEMOUNT_KIT = 0
GOLD = 1

class DemountOptionalDeviceDialog(DialogTemplateView):
    __slots__: tuple
    _wallet: Any
    _itemsCache: Any
    __item: Any
    removalPrice: Any
    __forFitting: Any
    __selector: Any
    __moneyOption: Any
    def __init__(self, itemCD, forFitting=False):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _inventorySyncHandler(self, *_):
        ...
    def _isSelected(self, index):
        ...
    def _select(self, index):
        ...
    def _getAdditionalData(self):
        ...
    def _isGoldEnough(self, gold=None):
        ...
    def _setResult(self, result):
        ...
