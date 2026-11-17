# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/data/MembersDataProvider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.DAAPIDataProvider import DAAPIDataProvider as DAAPIDataProvider
from messenger import g_settings as g_settings
from messenger.m_constants import USER_GUI_TYPE as USER_GUI_TYPE
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage

class MembersDataProvider(DAAPIDataProvider):
    usersStorage: Any
    __list: Any
    def __init__(self):
        ...
    @property
    def collection(self):
        ...
    def buildList(self, members):
        ...
    def emptyItem(self):
        ...
