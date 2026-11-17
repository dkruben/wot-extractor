# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/festivity/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from pprint import pformat as pformat
import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
_logger: Any

class BaseFestivityRequester(AbstractSyncDataRequester):
    dataKey = None
    def _requestCache(self, callback=None):
        ...
    def _preprocessValidData(self, data):
        ...

class BaseFestivityProcessor(object):
    __commandProxy: Any
    def __init__(self):
        ...
    def setCommandProxy(self, account):
        ...
    def _perform(self, command, argsList, callback=None):
        ...

def _defaultLogger(*args):
    ...
def _getProxy(callback):
    ...
