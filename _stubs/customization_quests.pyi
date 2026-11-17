# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/customization_quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
from collections import namedtuple as namedtuple
import persistent_data_cache_common as pdc
from quest_cache_helpers import readQuestsFromFile as readQuestsFromFile
from quest_xml_source import collectSections as collectSections, QuestValidationSerializer as QuestValidationSerializer
from constants import EVENT_TYPE as EVENT_TYPE
C11N_QUESTS_PROGRESSION_SOURCE_PATH: list
CustomizationQuest: Any
g_cust_cache = None

def customizationQuestsFromFile(pathToFiles, auxData=None):
    ...
def _createCache():
    ...
def init():
    ...
