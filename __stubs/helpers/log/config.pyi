# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/log/config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import logging.config
import os as os
from future.utils import viewvalues as viewvalues
import BWLogging as BWLogging
import resource_helper as resource_helper
from helpers.log import handlers as handlers
from helpers.log import hooks as hooks
ENV_KEY = 'PY_LOGGING_CFG'
XML_CFG_FILE = 'logging.xml'

class LogConfigurator(logging.config.DictConfigurator):
    importer: Any
    def clear(self):
        ...
    @classmethod
    def _clearConvertor(cls, convertor):
        ...

def setupFromXML(envKey=..., filename=..., level=...):
    ...
def readXMLConfig(filename):
    ...
def _readConfigItem(key, ctx, section):
    ...
