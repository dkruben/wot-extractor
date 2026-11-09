# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/log/handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import sys as sys
import traceback as traceback
from contextlib import closing as closing
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from py2to3.moves.io import FastStringIO as FastStringIO
_LOG_LEVEL_2_BW_FUNCTION: dict

class WotFormatter(logging.Formatter):
    def formatException(self, ei):
        ...

class WotExtendedFormatter(WotFormatter):
    _frameSize: Any
    def __init__(self, fmt=None, datefmt=None, frameSize=-1):
        ...
    def formatException(self, ei):
        ...

class WotLogHandler(logging.Handler):
    def emit(self, record):
        ...
