# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/doc_loaders/WindowsStoredDataLoader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.moves import pickle as pickle
from future.utils import lmap as lmap
import Settings as Settings
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from py2to3.compat import base64compat as base64compat

class WindowsStoredDataLoader(object):
    __rev: Any
    __maxRecordLen: Any
    __defMask: Any
    def __init__(self, rev, maxRecordLen, defMask):
        ...
    def load(self):
        ...
    def flush(self, mask, records):
        ...
