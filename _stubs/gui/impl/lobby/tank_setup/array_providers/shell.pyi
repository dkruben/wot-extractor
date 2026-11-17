# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/array_providers/shell.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_slot_model import ShellSlotModel as ShellSlotModel
from gui.impl.lobby.tank_setup.array_providers.base import VehicleBaseArrayProvider as VehicleBaseArrayProvider
from gui.impl.lobby.tank_setup.tank_setup_helper import createShellSpecificationModel as createShellSpecificationModel
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder as BuyPriceModelBuilder
from gui.shared.items_parameters.shell_mechanics_helper import getShellParameters as getShellParameters
from gui.shared.items_parameters.shell_params import BASE_SHELL_PARAMETERS as BASE_SHELL_PARAMETERS, getMechanicParameters as getMechanicParameters
from post_progression_common import TankSetupGroupsId as TankSetupGroupsId
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class ShellProvider(VehicleBaseArrayProvider):
    __slots__: tuple
    _itemsCache: Any
    def updateItems(self):
        ...
    def getItemViewModel(self):
        ...
    def fillArray(self, array, ctx, itemFilter=None):
        ...
    def updateArray(self, array, ctx):
        ...
    def createSlot(self, item, ctx):
        ...
    def updateSlot(self, model, item, ctx):
        ...
    def _fillSpecification(self, model, item):
        ...
