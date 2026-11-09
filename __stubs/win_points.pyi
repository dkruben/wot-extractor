# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/win_points.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from constants import FLAG_TYPES as FLAG_TYPES
from soft_exception import SoftException as SoftException
_CONFIG_FILE = 'scripts/item_defs/win_points.xml'
WinPointsTeamSettings = WinPointsTeamOrSoloSettings
WinPointsSoloSettings = WinPointsTeamOrSoloSettings
g_cache = None

class DamageSettings(object):
    pointsForKill: Any
    pointsForDamage: Any
    def __init__(self, section):
        ...

class WinPointsTeamOrSoloSettings(object):
    vehicleDamageSettings: Any
    equipmentDamageSettings: Any
    pointsForFlag: Any
    pointsForOneResource: Any
    def __init__(self, section):
        ...

class WinPointsSettings(object):
    pointsCAP: Any
    teamSettings: Any
    soloSettings: Any
    def __init__(self, section):
        ...
    def pointsForKill(self, isSolo, forVehicle):
        ...
    def pointsForDamage(self, isSolo, forVehicle):
        ...
    def __getattr__(self, item):
        ...

def init():
    ...
