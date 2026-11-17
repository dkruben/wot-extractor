# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/battle_pass_integration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import copy as copy
from collections import namedtuple as namedtuple
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES
from items import vehicles as vehicles
from soft_exception import SoftException as SoftException
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Type as Type, Union as Union
NON_VEH_CD = 0
BpPointsSettings: Any
_BATTLEPASS_BY_GAMEMODE: dict

class BattlePassIntegrationInterface(object):
    __slots__: tuple
    def getTeamSize(self):
        ...
    def validatePoints(self, season):
        ...
    def calculatePointsSettings(self, storage):
        ...

class BattlePassIntegrationRandom(BattlePassIntegrationInterface):
    __slots__: tuple
    teamSize: Any
    bonusTypeName: Any
    bonusType: Any
    def __init__(self, teamSize, bonusTypeName):
        ...
    def getTeamSize(self):
        ...
    def validatePoints(self, season):
        ...
    def calculatePointsSettings(self, storage):
        ...

class BattlePassIntegrationEpicBattle(BattlePassIntegrationRandom):
    __slots__: tuple
    def calculatePointsSettings(self, storage):
        ...
    def validatePoints(self, season):
        ...

class BattlePassIntegrationBattleRoyale(BattlePassIntegrationRandom):
    __slots__: tuple
    twinBonusType: Any
    def __init__(self, teamSize, bonusTypeName):
        ...
    def validatePoints(self, season):
        ...
    def calculatePointsSettings(self, storage):
        ...
    @staticmethod
    def _checkBattleRoyalePointsSequence(points, thresholdTargetCount):
        ...

class BattlePassIntegrationComp7Base(BattlePassIntegrationRandom):
    def calculatePointsSettings(self, storage):
        ...

class BattlePassIntegrationComp7(BattlePassIntegrationComp7Base):
    ...

class BattlePassIntegrationComp7Light(BattlePassIntegrationComp7Base):
    ...

def getBattlePassByGameMode(arenaBonusType):
    ...
def getAllIntergatedGameModes():
    ...
