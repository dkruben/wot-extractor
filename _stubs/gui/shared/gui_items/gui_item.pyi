# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/gui_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import total_ordering as total_ordering
from past.builtins import cmp as cmp
import nations as nations
from gui.impl import backport as backport
from gui.impl.gen import R as R
from items import ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, vehicles as vehicles
from gui import nationSortKeyByIndex as nationSortKeyByIndex
from helpers import dependency as dependency
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from soft_exception import SoftException as SoftException

# decorador original: @total_ordering
class HasIntCD(object):
    __slots__: tuple
    __hash__ = None
    intCompactDescr: Any
    itemTypeID: Any
    nationID: Any
    innationID: Any
    def __init__(self, intCompactDescr):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    @property
    def intCD(self):
        ...
    @property
    def itemTypeName(self):
        ...
    @property
    def nationName(self):
        ...
    @property
    def nationUserName(self):
        ...
    def _parseIntCompDescr(self, intCompactDescr):
        ...
    def __compare(self, other):
        ...

class HasStrCD(object):
    __slots__: tuple
    strCompactDescr: Any
    def __init__(self, strCompactDescr):
        ...
    @property
    def strCD(self):
        ...

# decorador original: @total_ordering
class GUIItem(object):
    __slots__: tuple
    __hash__ = None
    itemsFactory: Any
    _intCD: Any
    _strCD: Any
    def __init__(self, intCD=None, strCD=None):
        ...
    def __repr__(self):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    @property
    def intCDO(self):
        ...
    @property
    def intCD(self):
        ...
    @property
    def strCD(self):
        ...
    @property
    def itemTypeID(self):
        ...
    @itemTypeID.setter
    def itemTypeID(self, typeID):
        ...
    @property
    def itemTypeName(self):
        ...
    @property
    def nationID(self):
        ...
    @property
    def innationID(self):
        ...
    @property
    def nationName(self):
        ...
    @property
    def nationUserName(self):
        ...
    def _compare(self, other):
        ...
