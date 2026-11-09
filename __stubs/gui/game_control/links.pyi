# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/links.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from gui import macroses as macroses
from debug_utils import LOG_ERROR as LOG_ERROR
from adisp import adisp_process as adisp_process, adisp_async as adisp_async

class URLMacros(object):
    __MACROS_PREFIX = '$'
    __asyncMacroses: Any
    __syncMacroses: Any
    __filter: Any
    __argsFilter: Any
    def __init__(self, allowedMacroses=None):
        ...
    def clear(self):
        ...
    def hasMarcos(self, url):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def parse(self, url, params=None, callback=...):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _replace(self, macros, args, params, callback):
        ...
    def _getUserMacrosName(self, macros):
        ...
