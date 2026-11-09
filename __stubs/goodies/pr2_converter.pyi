# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/pr2_converter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from math import ceil as ceil
from typing import TYPE_CHECKING as TYPE_CHECKING
from future.utils import viewitems as viewitems
from typing import List as List, Tuple as Tuple
ConversionDataType: Any
XP = 121001
CRED = 121003
XP_CREW_FREE = 121005
XP_DEF = 121000
CRED_DEF = 121002
XP_CREW_FREE_DEF = 121004
ADVANCED_ITEMS: tuple
_NEW_ID_TO_OLD_IDS: dict
_OLD_ID_TO_NEW_ID: dict

class BType(object):
    GOLD = 10
    CREDITS = 20
    XP = 30
    CREW_XP = 40
    FREE_XP = 50
    FL_XP = 60
    FREE_XP_CREW_XP = 70

class IPR2ConversionDataBridge(object):
    def iterTargetItems(self):
        ...
    def getItemData(self, uid):
        ...
    def isAdvancedItem(self, uid):
        ...
    def applySingleItemsResult(self, resultList):
        ...

class PR2Converter(object):
    def convert(self, cDataProvider):
        ...
    def __getResultConversionData(self, oldID, cDataProvider):
        ...

def postConversionByType(convertedByState):
    ...
