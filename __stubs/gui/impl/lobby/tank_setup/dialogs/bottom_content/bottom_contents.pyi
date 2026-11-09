# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/bottom_content/bottom_contents.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.lobby.tank_setup.configurations.base import BaseDealPanel as BaseDealPanel
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder as BuyPriceModelBuilder
from gui.shared.gui_items.fitting_item import canBuyWithGoldExchange as canBuyWithGoldExchange
from gui.shared.gui_items.processors.vehicle import VehicleAutoRepairProcessor as VehicleAutoRepairProcessor
from gui.shared.money import Money as Money
from helpers import dependency as dependency
from gui.shared.utils import decorators as decorators
from skeletons.gui.shared import IItemsCache as IItemsCache

class AmmunitionBuyBottomContent(BaseSubModelView):
    __items: Any
    __vehicle: Any
    def __init__(self, viewModel, vehicle, items):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def update(self):
        ...

class PriceBottomContent(BaseSubModelView):
    __itemsCache: Any
    __price: Any
    __defPrice: Any
    def __init__(self, viewModel, price, defPrice=None):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def update(self, price=None, defPrice=None):
        ...

class NeedRepairBottomContent(PriceBottomContent):
    __vehicle: Any
    __price: Any
    __autoRepair: Any
    def __init__(self, viewModel, vehicle):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def update(self, price=None, defPrice=None):
        ...
    def __updateAutoRepair(self, args):
        ...
    # decorador original: @decorators.adisp_process(...)
    def processAutoRepair(self):
        ...
