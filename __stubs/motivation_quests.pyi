# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/motivation_quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
from pprint import pformat as pformat
from quest_cache_helpers import readQuestsFromFile as readQuestsFromFile, makeI18nString as makeI18nString
from constants import ITEM_DEFS_PATH as ITEM_DEFS_PATH, EVENT_TYPE as EVENT_TYPE
from debug_utils import LOG_WARNING as LOG_WARNING
_QUESTS_DIR: Any
_QUESTS_FILE = 'quests.xml'
g_cache = None

class MotivationQuest(object):
    __slots__: tuple
    questID: Any
    questName: Any
    questDescr: Any
    advice: Any
    requirements: Any
    congratulation: Any
    questData: Any
    def __init__(self, questID, questName, questDescr, advice, requirements, congratulation, questData):
        ...

class _QuestsCache(object):
    __quests: Any
    def __init__(self, quests):
        ...
    def getAllQuests(self):
        ...
    def getQuestIDs(self):
        ...
    def getQuestByID(self, questID):
        ...
    def __repr__(self):
        ...

def __parseMotivationsQuest(node):
    ...
def motivationQuestsFromFile(pathToFile):
    ...
def init():
    ...
