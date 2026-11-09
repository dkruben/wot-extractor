# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/premacc/premacc_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from helpers import time_utils as time_utils
_logger: Any

class BattleResultsBonusConstants(object):
    MAX_MULTIPLIER = 5
    MIN_MULTIPLIER = 1
    LOST_BATTLE_BACKGROUND_MULTIPLIER = 1

class PiggyBankConstants(object):
    MAX_AMOUNT = 750000
    SMASH_MAX_DELAY = 300
    OPEN_SOON_THRESHOLD_DEFAULT = 86400
    PIGGY_BANK_CREDITS = 'piggyBank.credits'
    PIGGY_BANK_GOLD = 'piggyBank.gold'
    PIGGY_BANK = 'piggyBank'
    PIGGY_BANK_SMASH_TIMESTAMP_CREDITS = 'piggyBank.lastSmashTimestamp'
    PIGGY_BANK_SMASH_TIMESTAMP_GOLD = 'piggyBank.lastSmashTimestampGold'

def validateAdditionalBonusMultiplier(multiplier):
    ...
def getOpenTimeHelper(config, data):
    ...
def getDeltaTimeHelper(config, data):
    ...
