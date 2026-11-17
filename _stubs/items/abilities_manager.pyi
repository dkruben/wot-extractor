# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/abilities_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import defaultdict as defaultdict, namedtuple as namedtuple
from operator import add as add
from future.utils import viewitems as viewitems
from items import perks as perks
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
_AbilityRecord: Any

class AbilitiesManager(object):
    DEFAULT_PRIORITY = 99
    _scopes: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def addBuild(self, vehInvID, scopeName, perksDict, priority=...):
        ...
    def modifyBuild(self, vehInvID, scopeName, modDict, operator=...):
        ...
    def getPerksByVehicle(self, vehInvID, perksMaxLevelConfig=None):
        ...
    def getPerksListByVehicle(self, vehInvID):
        ...
    def getPerkLevelByVehicle(self, vehInvID, scopeName, perkID):
        ...
    def getScopesNames(self, vehInvID):
        ...
    def removePerksByVehicle(self, vehInvID):
        ...
    def reset(self):
        ...

class PerksMaxLevelConfig(object):
    _config: Any
    _bonusType: Any
    def __init__(self, config, bonusType=None):
        ...
    def getMaxPerkLevel(self, perkID, default=None):
        ...
    def _getMaxPerkLevelFromConfig(self, config, perkID):
        ...
