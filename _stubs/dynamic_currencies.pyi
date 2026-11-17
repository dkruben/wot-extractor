# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dynamic_currencies.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from hashlib import md5 as md5
from typing import Dict as Dict
g_dynamicCurrenciesData: Any

class DynamicCurrenciesData:
    __currencies: Any
    __loaded: Any
    def __init__(self):
        ...
    def getData(self):
        ...
    def setData(self, data):
        ...
    def replaceData(self, data):
        ...
    @property
    def loaded(self):
        ...
    def isCurrencyCodeCorrect(self, currencyCode):
        ...

def getCurrencyCD(currencyCode):
    ...
