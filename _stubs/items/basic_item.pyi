# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/basic_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from items import ITEM_TYPE_NAMES as ITEM_TYPE_NAMES
from items.components import legacy_stuff as legacy_stuff, shared_components as shared_components, component_constants as component_constants
_LONG_DESCR_PROPERTY = 'longDescriptionSpecial'
_SHORT_DESCR_PROPERTY = 'shortDescriptionSpecial'

class BasicItem(legacy_stuff.LegacyStuff):
    __slots__: tuple
    typeID: Any
    id: Any
    name: Any
    compactDescr: Any
    tags: Any
    i18n: Any
    def __init__(self, typeID, itemID, itemName, compactDescr):
        ...
    def __repr__(self):
        ...
    @property
    def itemTypeName(self):
        ...
    @property
    def userString(self):
        ...
    @property
    def shortUserString(self):
        ...
    @property
    def description(self):
        ...
    @property
    def shortDescriptionSpecial(self):
        ...
    @property
    def longDescriptionSpecial(self):
        ...
    def _getDescription(self, descr):
        ...
    def copy(self):
        ...
