# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/core/log.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
import constants as constants
from helpers import time_utils as time_utils
from uilogging.core.common import getClientBuildVersion as getClientBuildVersion, convertEnum as convertEnum
from uilogging.constants import LogLevels as LogLevels, DEFAULT_LOGGER_NAME as DEFAULT_LOGGER_NAME
from uilogging.types import FeatureType as FeatureType, GroupType as GroupType, ActionType as ActionType, LogLevelType as LogLevelType
_logger: Any

class LogRecord(object):
    __slots__: tuple
    _properties: Any
    def __init__(self, feature, group, action, level, params):
        ...
    @property
    def feature(self):
        ...
    @property
    def group(self):
        ...
    @property
    def action(self):
        ...
    @property
    def level(self):
        ...
    @property
    def time(self):
        ...
    @property
    def partnerID(self):
        ...
    @property
    def broken(self):
        ...
    def toDict(self):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...
    def __len__(self):
        ...
