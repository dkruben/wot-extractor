# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/wrappers/user_drop_down_menu_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.impl.gen.view_models.ui_kit.drop_down_menu_item_model import DropDownMenuItemModel as DropDownMenuItemModel
from gui.impl.wrappers.user_list_model import UserListModel as UserListModel
_logger: Any

class UserDropDownMenuModel(UserListModel):
    __slots__: tuple
    def addItem(self, actionID, label, icon=None, isEnabled=True):
        ...
    def getItemByID(self, actionID):
        ...
