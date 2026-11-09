# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/popovers/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER as TYPES_ORDER
ItemsGroupVO: Any

class C11nPopoverItemData(object):
    __slots__: tuple
    item: Any
    season: Any
    slotsIds: Any
    isBase: Any
    isRemovable: Any
    isRemoved: Any
    isFromInventory: Any
    def __init__(self, item, season=None, isBase=False, isRemovable=False, isRemoved=False, isFromInventory=False):
        ...

def orderKey(itemData):
    ...
