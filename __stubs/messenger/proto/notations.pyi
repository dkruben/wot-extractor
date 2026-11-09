# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/notations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_NOTE as LOG_NOTE
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE_NAMES as PROTO_TYPE_NAMES

class _profile(object):
    _protoType: Any
    _doLog: Any
    def __init__(self, protoType, log=True):
        ...
    def __call__(self, func):
        ...
    def isEnabled(self):
        ...
    def log(self, name):
        ...

class contacts(_profile):
    def isEnabled(self):
        ...
    def log(self, name):
        ...
