# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/instructions/booster_buy_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import SystemMessages as SystemMessages
from gui.impl.gen import R as R
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.instructions.booster_buy_model import BoosterBuyModel as BoosterBuyModel
from gui.impl.lobby.common.buy_sell_item_base_dialog import DialogBuySellItemBaseView as DialogBuySellItemBaseView
from gui.shared.gui_items.processors.module import ModuleBuyer as ModuleBuyer
from gui.shared.gui_items.processors.vehicle import VehicleAutoBattleBoosterEquipProcessor as VehicleAutoBattleBoosterEquipProcessor
from adisp import adisp_process as adisp_process
from helpers.func_utils import oncePerPeriod as oncePerPeriod

class BoosterBuyWindowView(DialogBuySellItemBaseView):
    def __init__(self, typeCompDescr, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def isBuying(self):
        ...
    def _onInventoryResync(self, *args, **kwargs):
        ...
    def _setBaseParams(self, model):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onSetIsRearm(self, args=None):
        ...
    # decorador original: @oncePerPeriod(...)
    # decorador original: @adisp_process
    def _onAcceptClicked(self):
        ...
    def __calculateMaxCount(self):
        ...
