# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/rent_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
GOLD_TO_CREDITS_CONVERSION_RATE = 400
CREDITS_TO_GOLD_CONVERSION_RATE: Any
RENT_TYPE_TO_DURATION: dict

class SeasonRentDuration(object):
    ENTIRE_SEASON = 1
    SEASON_CYCLE = 2

def makeRentID(rentType, packageID):
    ...
def parseRentID(rentID):
    ...
def calculateSeasonRentPrice(priceForLastCycle, priceForSeason, currentCycleIdx, numCycles):
    ...
def isWithinMaxRentTime(maxRentDuration, rentLeftTime, daysToRent):
    ...
