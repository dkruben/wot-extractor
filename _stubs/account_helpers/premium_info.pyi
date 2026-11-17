# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/premium_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREMIUM_TYPE as PREMIUM_TYPE

class PremiumInfo(object):
    _rawPremiumInfo: Any
    def __init__(self):
        ...
    def update(self, rawPremiumInfo):
        ...
    def isActivePremium(self, checkPremiumType):
        ...
    @property
    def isPremium(self):
        ...
    @property
    def totalPremiumExpiryTime(self):
        ...
    @property
    def activePremiumExpiryTime(self):
        ...
    @property
    def activePremiumType(self):
        ...
    @property
    def data(self):
        ...
