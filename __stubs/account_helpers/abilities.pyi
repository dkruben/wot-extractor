# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/abilities.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
import AccountCommands as AccountCommands
from items.abilities_manager import AbilitiesManager as AbilitiesManager

class AbilitiesHelper(object):
    __account: Any
    __ignore: Any
    __abilities: Any
    def __init__(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    @property
    def abilitiesManager(self):
        ...
    def addPerks(self, battle, vehicleID, scopeIndex, perksList, callback=None):
        ...
    def resetPerks(self, battle, vehicleID, callback=None):
        ...
