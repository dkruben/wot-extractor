# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/quest_cache_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
from constants import EVENT_TYPE as EVENT_TYPE, IS_CLIENT as IS_CLIENT
from debug_utils import LOG_WARNING as LOG_WARNING
import quest_xml_source as quest_xml_source
from soft_exception import SoftException as SoftException
from helpers import i18n as i18n
from web_stubs import i18n as i18n
_logger: Any

def makeI18nString(string):
    ...
def _getEventName(eventType):
    ...
def readQuestsFromFile(filePath, eventType, auxData=None):
    ...
