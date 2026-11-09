# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/rage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from items import vehicles as vehicles
_CONFIG_FILE = 'scripts/item_defs/rage.xml'
RageTeamSettings = RageTeamOrSoloSettings
RageSoloSettings = RageTeamOrSoloSettings
g_cache = None

class DamageSettings(object):
    damageFactor: Any
    pointsForKill: Any
    def __init__(self, section):
        ...

class RageTeamOrSoloSettings(object):
    vehicleDamageSettings: Any
    equipmentDamageSettings: Any
    pointsForFlagPickup: Any
    pointsForFlagCapture: Any
    pointsForOneResource: Any
    deathPenalty: Any
    def __init__(self, section):
        ...

class RageSettings(object):
    pointsLimit: Any
    equipments: Any
    teamSettings: Any
    soloSettings: Any
    def __init__(self, section):
        ...
    def damageFactor(self, isSolo, forVehicle):
        ...
    def pointsForKill(self, isSolo, forVehicle):
        ...
    def __getattr__(self, item):
        ...

def init():
    ...
