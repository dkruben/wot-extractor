# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/simple_stats_parameter_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen import R as R

class ValueType(IntEnum):
    INTEGER = 0
    FLOAT = 1
    TIME = 2

class RegularParamType(Enum):
    SHOTS = 'shots'
    HITS = 'hits'
    EXPLOSIONHITS = 'explosionHits'
    DAMAGEDEALT = 'damageDealt'
    SNIPERDAMAGEDEALT = 'sniperDamageDealt'
    ARTILLERYSTRIKE = 'artilleryStrike'
    DIRECTHITSRECEIVED = 'directHitsReceived'
    PIERCINGSRECEIVED = 'piercingsReceived'
    NODAMAGEDIRECTHITSRECEIVED = 'noDamageDirectHitsReceived'
    EXPLOSIONHITSRECEIVED = 'explosionHitsReceived'
    DAMAGEBLOCKEDBYARMOR = 'damageBlockedByArmor'
    TEAMHITSDAMAGE = 'teamHitsDamage'
    SPOTTED = 'spotted'
    DAMAGEDKILLED = 'damagedKilled'
    DAMAGEASSISTED = 'damageAssisted'
    DAMAGEASSISTEDSELF = 'damageAssistedSelf'
    STUNDURATION = 'stunDuration'
    DAMAGEASSISTEDSTUN = 'damageAssistedStun'
    DAMAGEASSISTEDSTUNSELF = 'damageAssistedStunSelf'
    STUNNUM = 'stunNum'
    CAPTUREPOINTSVAL = 'capturePointsVal'
    MILEAGE = 'mileage'

class SimpleStatsParameterModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getLabel(self):
        ...
    def setLabel(self, value):
        ...
    def getLabelKey(self):
        ...
    def setLabelKey(self, value):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    @staticmethod
    def getValueType():
        ...
    def getParamValueType(self):
        ...
    def setParamValueType(self, value):
        ...
    def _initialize(self):
        ...
