# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/contents/multiple_items_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen.view_models.constants.fitting_types import FittingTypes as FittingTypes
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.lobby.dialogs.auxiliary.confirmed_items_packer import ConfirmedItemsPacker as ConfirmedItemsPacker
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel as MultipleItemsContentModel
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem

class MultipleItemsContent(BaseSubModelView):
    __slots__: tuple
    _items: Any
    _confirmedItemsPacker: Any
    _itemsType: Any
    def __init__(self, viewModel, items, vehicleInvID=None, itemsType=None):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def _fillItems(self, array):
        ...
    def _determineItemsType(self, items):
        ...
