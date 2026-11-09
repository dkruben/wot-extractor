# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/main_content/main_contents.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen.view_models.constants.fitting_types import FittingTypes as FittingTypes
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_helpers import ConfirmedItemWarningTypes as ConfirmedItemWarningTypes
from gui.impl.lobby.dialogs.contents.multiple_items_content import MultipleItemsContent as MultipleItemsContent
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.ammunition_buy_helper import modulesSortFunction as modulesSortFunction
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.ammunition_buy_content import AmmunitionBuyContent as AmmunitionBuyContent
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria

class AmmunitionBuyMainContent(MultipleItemsContent):
    __slots__: tuple
    __filterCriteria: Any
    def __init__(self, viewModel, items, itemsType=None, vehicleInvID=None, filterCriteria=None):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def updateFilter(self, filterCriteria):
        ...
    def _fillItems(self, array):
        ...
    def __lacksItem(self, array):
        ...

class NeedRepairMainContent(BaseSubModelView):
    _repairPercentage: Any
    vehicle: Any
    def __init__(self, viewModel, repairPercentage, vehicle):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def update(self, repairPercentage=None):
        ...
