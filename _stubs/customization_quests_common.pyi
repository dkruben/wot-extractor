# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/customization_quests_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict, Optional as Optional
from copy import deepcopy as deepcopy
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from items import vehicles as vehicles
from constants import CUSTOMIZATION_PROGRESS_PREFIX as PREFIX, EVENT_TYPE as EVENT_TYPE
from items.components.c11n_components import CustomizationType as CustomizationType, QuestProgressForCustomization as qpc
SEPARATOR = '_'
TEMPLATE: Any

class CustQuestsCache(object):
    __slots__: tuple
    _groupByToken: Any
    def __init__(self, groupByToken=None):
        ...
    def addQuest(self, et, quest):
        ...
    def setFinishTime(self, tokenId, level, finishTime):
        ...
    def __iter__(self):
        ...
    def asDict(self):
        ...
    def copy(self):
        ...
    def updateQuests(self, custQuestCache):
        ...

def validateToken(token):
    ...
def serializeToken(styleId, group):
    ...
def deserializeToken(token):
    ...
def validateCustomizationQuestToken(id, token):
    ...
