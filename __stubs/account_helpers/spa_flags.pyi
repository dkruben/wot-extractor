# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/spa_flags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from external_strings_utils import strtobool as strtobool, InvalidStringValueException as InvalidStringValueException
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from constants import SPA_ATTRS as SPA_ATTRS

class SPAFlags(object):
    __account: Any
    __syncData: Any
    __cache: Any
    __country: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self, diff):
        ...
    def getFlag(self, flagName):
        ...
    def getCountry(self):
        ...
