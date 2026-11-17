# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/mods_statistic/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from wotdecorators import noexcept as noexcept
_logger: Any

class ModsStatisticLogger(Logger):
    FEATURE_NAME = 'mods_statistic'
    GROUP_NAME = 'mods_statistic'
    ACTION = 'collected'
    MAX_JSON_STR_LEN = 10000
    MD5_LEN = 32
    __alreadyLogged = False
    def __init__(self):
        ...
    # decorador original: @noexcept
    def log(self):
        ...
