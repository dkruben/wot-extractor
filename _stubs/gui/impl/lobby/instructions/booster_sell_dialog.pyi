# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/instructions/booster_sell_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleMeta import MAX_ITEMS_FOR_OPERATION as MAX_ITEMS_FOR_OPERATION
from gui.impl.gen.view_models.views.lobby.common.buy_sell_items_dialog_model import BuySellItemsDialogModel as BuySellItemsDialogModel
from gui.impl.lobby.common.buy_sell_item_base_dialog import DialogBuySellItemBaseView as DialogBuySellItemBaseView
from gui.impl.gen import R as R
from frameworks.wulf import ViewSettings as ViewSettings
from gui.shared.gui_items.processors.module import ModuleSeller as ModuleSeller
from adisp import adisp_process as adisp_process

class BoosterSellWindowView(DialogBuySellItemBaseView):
    def __init__(self, typeCompDescr, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def isBuying(self):
        ...
    def _setBaseParams(self, model):
        ...
    # decorador original: @adisp_process
    def _onAcceptClicked(self):
        ...
