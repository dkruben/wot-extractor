# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/prebattle_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from future.utils import lfilter as lfilter, viewitems as viewitems, viewvalues as viewvalues
import nations as nations
from items import vehicles as vehicles, ITEM_TYPES as ITEM_TYPES
from items.badges_common import BadgesCommon as BadgesCommon
from account_shared import AmmoIterator as AmmoIterator
from constants import PREBATTLE_ACCOUNT_STATE as PREBATTLE_ACCOUNT_STATE, VEHICLE_CLASSES as VEHICLE_CLASSES, ARENA_GUI_TYPE as ARENA_GUI_TYPE, PREBATTLE_ROLE as PREBATTLE_ROLE, IGR_TYPE as IGR_TYPE, IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG as LOG_DEBUG
from typing import Any as Any, Dict as Dict
SETTING_DEFAULTS: dict
LIMIT_DEFAULTS: dict

class PrebattleSettings(object):
    __settings: _Any
    def __init__(self, settings):
        ...
    def __getitem__(self, key):
        ...
    def __setitem__(self, key, value):
        ...
    def getTeamLimits(self, team):
        ...

class TeamLimits(object):
    __limits: _Any
    __team: _Any
    def __init__(self, settings, team):
        ...
    def __getitem__(self, key):
        ...

def decodeRoster(roster):
    ...
def encodeRoster(team, assigned):
    ...
def isVehicleValid(vehDescr, vehAmmo, limits):
    ...
def isObserver(vehCompDescr):
    ...
def isTeamValid(accountsInfo, limits):
    ...
def _collectCurrentReplaceableVehicleComponents(vehicleDescr):
    ...
def getClanWarsExtraEquipments(clansEquipments, joinedAccountsDBIDs, prebattleID):
    ...
