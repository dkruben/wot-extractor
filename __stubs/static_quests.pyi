# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/static_quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import logging as logging
from collections import namedtuple as namedtuple
import typing as typing
import persistent_data_cache_common as pdc
from ExtensionsManager import g_extensionsManager as g_extensionsManager
from constants import EVENT_TYPE as EVENT_TYPE
from quest_cache_helpers import readQuestsFromFile as readQuestsFromFile
from quest_xml_source import collectSections as collectSections
STATIC_QUEST_SOURCE_PATH: list
_logger: Any
StaticQuest: Any
g_staticCache = None

class _StaticQuestsCache(object):
    __quests: Any
    def __init__(self, quests):
        ...
    def getAllQuests(self):
        ...
    def getQuestByID(self, questID):
        ...

def __isServerOnlyQuest(node):
    ...
def __getStaticQuestsFromFileByEventType(sectionList, eventType, auxData=None):
    ...
def __staticQuestsFromFile(sectionList, auxData=None):
    ...
def _createCache():
    ...
def init():
    ...
