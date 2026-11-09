# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/persistent_caches.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import os as os
from future.moves import pickle as pickle
import BigWorld as BigWorld
import constants as constants
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
from py2to3.compat import base64compat as base64compat
from soft_exception import SoftException as SoftException

class SimpleCache(object):
    __cacheType: Any
    __cacheName: Any
    __account: Any
    __memcache: Any
    def __init__(self, cacheType, cacheName):
        ...
    def clear(self):
        ...
    def setAccount(self, account=None):
        ...
    def getAccount(self):
        ...
    def getFileName(self):
        ...
    def get(self):
        ...
    def getDescr(self):
        ...
    def getData(self):
        ...
    def __load(self):
        ...
    def save(self, descr, data):
        ...

def cacheFileName(account, cacheType, cacheName):
    ...
def readFile(filename):
    ...
def writeFile(filename, data):
    ...
