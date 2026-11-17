# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/preview_bottom_panel_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from enum import Enum as Enum
from gui.impl.gen import R as R
_logger: Any
ObtainingMethodInfo: Any
SHOWCASE_STYLE_OBTAINING_METHOD_INFO: dict
ITEM_PACK_OBTAINING_METHOD_INFO: dict

class _Enum(Enum):
    @classmethod
    def hasValue(cls, value):
        ...

class ObtainingMethods(_Enum):
    BUY = 'buy'
    OBTAIN_FOR_COINS = 'obtain_for_coins'
    OBTAIN_FOR_FREE = 'obtain_for_free'

def getItemPackObtainingInfo(obtainingMethod=...):
    ...
def getShowcaseStyleObtainingInfo(obtainingMethod=...):
    ...
