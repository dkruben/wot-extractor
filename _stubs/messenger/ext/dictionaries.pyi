# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/ext/dictionaries.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import sre_compile as sre_compile
from future.utils import viewitems as viewitems
from past.builtins import unicode as unicode
import ResMgr as ResMgr
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from helpers import html as html
_defaultReplacementFunction: Any

class ObsceneLanguageDictionary(object):
    replace: Any
    @staticmethod
    def overrideReplacementFunction(function):
        ...
    @staticmethod
    def resetReplacementFunction():
        ...
    def searchAndReplace(self, text):
        ...

class BasicOLDictionary(ObsceneLanguageDictionary):
    __nonAlphaNumPattern: Any
    __equivalents: dict
    __badWordPatterns: list
    @classmethod
    def load(cls, resourceId):
        ...
    def searchAndReplace(self, text):
        ...

class SpecialOLDictionary(ObsceneLanguageDictionary):
    __badWordPatterns: list
    @classmethod
    def load(cls, resourceId):
        ...
    def searchAndReplace(self, text):
        ...

class ChinaOLDictionary(SpecialOLDictionary):
    __badWordPatterns: list
    __equivalents: dict
    @classmethod
    def load(cls, resourceId):
        ...
    def searchAndReplace(self, text):
        ...

class DomainNameDictionary(object):
    __webPrefix = '^(http(s)?://)?(www\\.)?'
    __domainNamePatterns: list
    replace: Any
    @classmethod
    def load(cls, resourceId):
        ...
    @staticmethod
    def overrideReplacementFunction(function):
        ...
    @staticmethod
    def resetReplacementFunction():
        ...
    def searchAndReplace(self, text):
        ...
