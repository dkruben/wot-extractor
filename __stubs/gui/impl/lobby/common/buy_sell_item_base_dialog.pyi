# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/buy_sell_item_base_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE
from gui.impl.gen.view_models.views.lobby.common.buy_sell_items_dialog_model import BuySellItemsDialogModel as BuySellItemsDialogModel

class DialogBuySellItemBaseView(FullScreenDialogView):
    _itemCD: Any
    _item: Any
    def __init__(self, settings, typeCompDescr):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def isBuying(self):
        ...
    def createToolTip(self, event):
        ...
    def _setBaseParams(self, model):
        ...
    def _getItemPrice(self):
        ...
    def _setItemPrices(self, model):
        ...
    def _finalize(self):
        ...
